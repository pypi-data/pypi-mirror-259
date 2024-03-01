#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Wed Apr  1 21:57:54 2020
# @author: Ajit Johnson Nirmal, Yuan Chen
"""
!!! abstract "Short Description"
    `sm.pl.image_viewer`: The function allows users to open OME-TIFF images inside 
    Napari and overlay any any categorical column such as cluster annotation or phenotypes.

## Function
"""

# %gui qt
try:
    import napari
except:
    pass
import pandas as pd
import random
import tifffile as tiff

import dask.array as da
from dask.cache import Cache
import zarr
import os

cache = Cache(2e9)  # Leverage two gigabytes of memory
cache.register()


def image_viewer(
    image_path,
    adata,
    overlay=None,
    flip_y=True,
    overlay_category=None,
    markers=None,
    channel_names='default',
    x_coordinate='X_centroid',
    y_coordinate='Y_centroid',
    point_size=10,
    point_color=None,
    subset=None,
    imageid='imageid',
    seg_mask=None,
    **kwargs,
):
    """
    Parameters:
        image_path (str):  
            Location to the image file (TIFF, OME.TIFF, ZARR supported)

        seg_mask (str):  
            Location to the segmentation mask file.

        adata (Ann Data Object):

        flip_y (bool):  
            Flip the Y-axis if needed. Some algorithms output the XY with the Y-coordinates flipped.
            If the image overlays do not align to the cells, try again by setting this to `False`.

        overlay (str):  
            Name of the column with any categorical data such as phenotypes or clusters.

        overlay_category (list):  
            If only specfic categories within the overlay column is needed, pass their names as a list.
            If None, all categories will be used.

        markers (list):  
            Markers to be included. If none, all markers will be displayed.

        channel_names (list):  
            List of channels in the image in the exact order as image. The default is `adata.uns['all_markers']`

        x_coordinate (str):  
            X axis coordinate column name in AnnData object.

        y_coordinate (str):  
            Y axis coordinate column name in AnnData object.

        point_size (int):  
            point size in the napari plot.

        point_color (str, dict):  
            The default behavior is to assign auto colors, but you can also provide
            a color mapping using the point_color parameter. For instance, you can pass a
            dictionary that maps color values to specific categories (provided in the `overlay` parameter).
            Here is an example of such a color mapping: `point_color = {'cellTypeA': '#FFFFFF', 'cellTypeB': '#000000'}`.
            A single color can also be provided like `point_color = 'white'`

        imageid (str):  
            Column name of the column containing the image id.

        subset (str):  
            imageid of a single image to be subsetted for analyis. Only useful when multiple images are being analyzed together.

        **kwargs
            Other arguments that can be passed to napari viewer

    Returns:
        Napari Viewer (image viewer):

    Example:
    ```python
        image_path = '/Users/aj/Desktop/ptcl_tma/image.ome.tif'
        sm.pl.image_viewer (image_path, adata, overlay='phenotype',overlay_category=None,
                    markers=['CD31', "CD3D","DNA11",'CD19','CD45','CD163','FOXP3'],
                    point_size=7,point_color='white')
    ```
    """

    # TODO
    # - ADD Subset markers for ZARR ssection
    # - Ability to use ZARR metadata if available

    # adding option to load just the image without an adata object
    if adata is None:
        channel_names = None
    else:
        # All operations on the AnnData object is performed first
        # Plot only the Image that is requested
        if subset is not None:
            adata = adata[adata.obs[imageid] == subset]

        # Recover the channel names from adata
        if channel_names == 'default':
            channel_names = adata.uns['all_markers']
        else:
            channel_names = channel_names

        # Index of the marker of interest and corresponding names
        if markers is None:
            idx = list(range(len(channel_names)))
            channel_names = channel_names
        else:
            idx = []
            for i in markers:
                idx.append(list(channel_names).index(i))
            channel_names = markers

        # Load the segmentation mask
        if seg_mask is not None:
            seg_m = tiff.imread(seg_mask)
            if (len(seg_m.shape) > 2) and (seg_m.shape[0] > 1):
                seg_m = seg_m[0]

    # Operations on the OME TIFF image is performed next
    # check the format of image
    if os.path.isfile(image_path) is True:
        image = tiff.TiffFile(image_path, is_ome=False)  # is_ome=False
        z = zarr.open(image.aszarr(), mode='r')  # convert image to Zarr array
        # Identify the number of pyramids
        n_levels = len(image.series[0].levels)  # pyramid

        # If and if not pyramids are available
        if n_levels > 1:
            pyramid = [da.from_zarr(z[i]) for i in range(n_levels)]
            multiscale = True
        else:
            pyramid = da.from_zarr(z)
            multiscale = False

        # subset channels of interest
        if markers is not None:
            if n_levels > 1:
                for i in range(n_levels - 1):
                    pyramid[i] = pyramid[i][idx, :, :]
                n_channels = pyramid[0].shape[0]  # identify the number of channels
            else:
                pyramid = pyramid[idx, :, :]
                n_channels = pyramid.shape[0]  # identify the number of channels
        else:
            if n_levels > 1:
                n_channels = pyramid[0].shape[0]
            else:
                n_channels = pyramid.shape[0]

        # check if channel names have been passed to all channels
        if channel_names is not None:
            assert n_channels == len(channel_names), (
                f'number of channel names ({len(channel_names)}) must '
                f'match number of channels ({n_channels})'
            )

        # Load the viewer
        viewer = napari.view_image(
            pyramid,
            multiscale=multiscale,
            channel_axis=0,
            visible=False,
            name=None if channel_names is None else channel_names,
            **kwargs,
        )

    # Operations on the ZARR image
    # check the format of image
    if os.path.isfile(image_path) is False:
        # print(image_path)
        viewer = napari.Viewer()
        viewer.open(
            image_path,
            multiscale=True,
            visible=False,
            name=None if channel_names is None else channel_names,
        )

    # Add the seg mask
    if seg_mask is not None:
        viewer.add_labels(seg_m, name='segmentation mask', visible=False)

    # Add phenotype layer function
    def add_phenotype_layer(
        adata,
        overlay,
        phenotype_layer,
        x,
        y,
        viewer,
        point_size,
        point_color,
        available_phenotypes,
    ):
        coordinates = adata[adata.obs[overlay] == phenotype_layer]
        # Flip Y AXIS if needed
        if flip_y is True:
            coordinates = pd.DataFrame(
                {'y': coordinates.obs[y], 'x': coordinates.obs[x]}
            )
        else:
            coordinates = pd.DataFrame(
                {'x': coordinates.obs[x], 'y': coordinates.obs[y]}
            )

        # points = coordinates.values.tolist()
        points = coordinates.values
        if point_color is None:
            r = lambda: random.randint(0, 255)  # random color generator
            point_color = '#%02X%02X%02X' % (r(), r(), r())  # random color generator
        elif isinstance(point_color, dict):
            # if dict identify the color for the given phenotype
            # also if a color is not provided in the dict assign it to white
            try:
                point_color = point_color[available_phenotypes]
            except KeyError:
                point_color = 'white'
                # if the dict has list, we need to account for it and so the following two lines
                if isinstance(point_color, list):
                    point_color = point_color[0]

        # check if point_color is a dict and if so isolate the color to the specific categoty
        viewer.add_points(
            points,
            size=point_size,
            face_color=point_color,
            visible=False,
            name=phenotype_layer,
        )

    if overlay is not None:
        # categories under investigation
        if overlay_category is None:
            available_phenotypes = list(adata.obs[overlay].unique())
        else:
            available_phenotypes = overlay_category

        # Run the function on all phenotypes
        for i in available_phenotypes:
            add_phenotype_layer(
                adata=adata,
                overlay=overlay,
                phenotype_layer=i,
                x=x_coordinate,
                y=y_coordinate,
                viewer=viewer,
                point_size=point_size,
                point_color=point_color,
                available_phenotypes=i,
            )
