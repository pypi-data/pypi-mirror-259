#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Sat Oct 24 13:07:38 2020
# @author: Ajit Johnson Nirmal
"""
!!! abstract "Short Description"
    `sm.pl.spatial_distance`: The function allows users to visualize the average shortest distance between phenotypes of interest.
    Run `sm.tl.spatial_distance` before running this function.

## Function
"""

# library
import pandas as pd
import matplotlib
import numpy as np
import seaborn as sns; sns.set(color_codes=True)
sns.set_style("white")


def spatial_distance (adata, spatial_distance='spatial_distance',phenotype='phenotype',imageid='imageid',log=False,
                      method='heatmap',heatmap_summarize=True,heatmap_na_color='grey',heatmap_cmap='vlag_r',
                      heatmap_row_cluster=False,heatmap_col_cluster=False,heatmap_standard_scale=0,
                      distance_from=None,distance_to=None,x_axis = None,y_axis = None,facet_by = None,plot_type = None,
                      return_data = False, subset_col=None, subset_value=None,
                      **kwargs):
    """
Parameters:

    adata : AnnData object

    spatial_distance : string, optional
        In order to locate the spatial_distance data within the AnnData object please provide the output
        label/columnname of `sm.tl.spatial_distance` function.

    phenotype : string, required
        Column name of the column containing the phenotype information.
        It could also be any categorical assignment given to single cells.

    imageid : string, optional
        Column name of the column containing the image id.

    log : bool, optional
        Convert distance to log scale.

    method : string, optional
        Three options are available.
        1) heatmap - generates a heatmap of average shortest distance between all phenotypes.
        2) numeric - can be used to generate boxplot, violin plot etc between a given set of phenotypes.
        3) distribution - can be used to generate distribution plots between a given set of phenotypes.

    heatmap_summarize : bool, optional
        In the event multiple images are present in the dataset, True allows to calculate the
        average across all the images.

    heatmap_na_color : string, optional
        Color for NA values within the heatmap.

    heatmap_cmap : string, optional
        Color map to use for continous variables.
        Can be a name or a Colormap instance (e.g. 'magma', 'viridis').

    heatmap_row_cluster : bool, optional
        Cluster Rows.

    heatmap_col_cluster : bool, optional
        Cluster Columns.

    heatmap_standard_scale : int, optional
        Either 0 (rows) or 1 (columns). Whether or not to standardize that dimension,
        meaning for each row or column, subtract the minimum and divide each by its maximum.

    distance_from : string, optional
        In the event of using method = 'numeric' or 'distribution', this argument is required.
        Pass a phenotype of interest. If distance_from is provided and distance_to is not provided,
        the function will plot the average distance from the phenotype of interest to all
        phenotypes present within the dataset.

    distance_to : string, optional
        In the event of using method = 'numeric' or 'distribution', this argument is required.
        Pass a phenotype of interest. The function will plot the average shortest between two phenotypes of
        interest (distance_from and distance_to).

    x_axis : string, optional
        In the event of using method = 'numeric' or 'distribution', this argument is required.
        This determines the elements present in the x-axis of the resultant plot.
        Allowed arguments are: 'group', 'distance', 'imageid'.

    y_axis : string, optional
        In the event of using method = 'numeric' or 'distribution', this argument is required.
        This determines the elements present in the y-axis of the numeric plot and if the user uses the distribution
        plot this argument is used to overlaying multiple categories within the same distribution plot.
        Allowed arguments are: 'group', 'distance', 'imageid'.

    facet_by : string, optional
         In the event of using method = 'numeric' or 'distribution', this argument can be used to
         generate sub-plots. Allowed arguments are: 'group', 'imageid'.

    plot_type : string, optional
        In the event of using method = 'numeric' or 'distribution', this argument is required.
        For `numeric` plot, the following options are available: “strip”, “swarm”, “box”, “violin”, “boxen”, “point”, “bar”, or “count”.
        For `distribution` plot, the following options are available: “hist”, “kde”, “ecdf”.
        The default for `numeric` plot is 'boxen'.
        The default for `distribution` plot is 'kde`.

    subset_col : string, optional
        If the users wants to consider only a subset of observations while plotting, this argument in conjuction to
        `subset_value` can be used.
        For example, in the event of a multi-image dataset, the `sm.tl.spatial_distance` was run on all images
        but the user is interested in plotting only a subset of images. Pass the name of the column which contains
        the categories to be subsetted.

    subset_value : list, optional
        If the users wants to consider only a subset of observations while plotting, this argument in conjuction to
        `subset_col` can be used. Pass a list of the categories to be subsetted.

    **kwargs : dict
        Are passed to sns.clustermap. Pass other parameters that works with `sns.clustermap`, `sns.catplot` or `sns.displot`
        e.g. `linecolor='black'`.

Returns:
    Heatmap or Numeric Plot or Distribution Plot.

Example:
```python
    # summary heatmap
    sm.pl.spatial_distance (adata)

    # Heatmap without summarizing the individual images
    sm.pl.spatial_distance (adata, heatmap_summarize=False,
    imageid='ImageId')

    # Numeric plot of shortest distance of phenotypes
    # from tumor cells
    sm.pl.spatial_distance (adata, method='numeric',
    distance_from='Tumor CD30+',imageid='ImageId')

    # Distribution plot of shortest distance of phenotypes
    # from tumor cells
    sm.pl.spatial_distance (adata, method='distribution',
    distance_from='Tumor CD30+',imageid='ImageId',
    x_axis="distance", y_axis="imageid", plot_type="kde")

    # Numeric plot of shortest distance of phenotypes from
    # tumor cells to M2 Macrophages
    sm.pl.spatial_distance (adata, method='numeric',
    distance_from='Tumor CD30+',distance_to = 'M2 Macrophages',
    imageid='ImageId')

    # Distribution plot of shortest distance of phenotypes from
    # tumor cells to M2 Macrophages
    sm.pl.spatial_distance (adata, method='distribution',
    distance_from='Tumor CD30+',distance_to = 'M2 Macrophages',
    imageid='ImageId')
```
    """


    # set color for heatmap
    cmap_updated = matplotlib.cm.get_cmap(heatmap_cmap)
    cmap_updated.set_bad(color=heatmap_na_color)


    # Copy the spatial_distance results from anndata object
    try:
        diatance_map = adata.uns[spatial_distance].copy()
    except KeyError:
        raise ValueError('spatial_distance not found- Please run sm.tl.spatial_distance first')

    # subset the data if user requests
    if subset_col is not None:
        if isinstance(subset_value, str):
            subset_value = [subset_value]
        # find the cell names to be subsetted out
        obs = adata.obs[[subset_col]]
        cells_to_subset = obs[obs[subset_col].isin(subset_value)].index

        # subset the diatance_map
        diatance_map = diatance_map.loc[diatance_map.index.intersection(cells_to_subset)]
        #diatance_map = diatance_map.loc[cells_to_subset]


    # Convert distance to log scale if user requests
    if log is True:
        diatance_map = np.log1p(diatance_map)

    # Method
    if method=='heatmap':
        if heatmap_summarize is True:
            # create the necessary data
            data = pd.DataFrame({'phenotype': adata.obs[phenotype]})
            data = pd.merge(data, diatance_map, how='outer',left_index=True, right_index=True) # merge with the distance map
            k = data.groupby(['phenotype']).mean() # collapse the whole dataset into mean expression
            d = k[k.index]
        else:
            # create new naming scheme for the phenotypes
            non_summary = pd.DataFrame({'imageid': adata.obs[imageid], 'phenotype': adata.obs[phenotype]})
            non_summary['imageid'] = non_summary['imageid'].astype(str) # convert the column to string
            non_summary['phenotype'] = non_summary['phenotype'].astype(str) # convert the column to string
            non_summary['image_phenotype'] = non_summary['imageid'].str.cat(non_summary['phenotype'],sep="_")
            # Merge distance map with phenotype
            data = pd.DataFrame(non_summary[['image_phenotype']])
            data = pd.merge(data, diatance_map, how='outer',left_index=True, right_index=True)
            k = data.groupby(['image_phenotype']).mean()
            d = k.sort_index(axis=1)
        # Generate the heatmap
        mask = d.isnull() # identify the NAN's for masking 
        d = d.fillna(0) # replace nan's with 0 so that clustering will work
        # Heatmap
        sns.clustermap(d, cmap=heatmap_cmap, row_cluster=heatmap_row_cluster,
                       col_cluster=heatmap_col_cluster, mask=mask,
                       standard_scale=heatmap_standard_scale, **kwargs)
    else:

        # condition-1
        if distance_from is None and distance_to is None:
            raise ValueError('Please include distance_from and/or distance_to parameters to use this method')

        # condition-2
        if distance_from is None and distance_to is not None:
            raise ValueError('Please `distance_from` parameters to use this method')

        # condition-3
        if distance_to is not None:
            # convert input to list if needed
            if isinstance(distance_to, str):
                distance_to = [distance_to]

        # Start
        pheno_df = pd.DataFrame({'imageid': adata.obs[imageid], 'phenotype': adata.obs[phenotype]}) #image id and phenotype
        data = pd.merge(pheno_df, diatance_map, how='outer',left_index=True, right_index=True) # merge with the distance map
        data = data[data['phenotype'] == distance_from] # subset the pheno of interest

        if distance_to is not None:
            data = data[distance_to] # drop columns that are not requested in distance_to
        else:
            data = data.drop(['phenotype','imageid'], axis=1) # drop the phenotype column before stacking

        d = data.stack().reset_index() # collapse everything to one column
        d.columns = ['cellid', 'group', 'distance']
        d = pd.merge(d, pheno_df, left_on='cellid', right_index=True) # bring back the imageid and phenotype

        # Convert columns to str
        for col in ['imageid', 'group','phenotype']:
            d[col] = d[col].astype(str)

        # Convert columns to categorical so that it drops unused categories
        for col in ['imageid', 'group','phenotype']:
            d[col] = d[col].astype('category')

        # re arrange the order based on from and to list provided
        if distance_to is not None:
            d['group'] = d['group'].cat.reorder_categories(distance_to)
            d = d.sort_values('group')

        # Plotting
        if method=='numeric':
            if x_axis is None and y_axis is None and facet_by is None and plot_type is None:
                sns.catplot(data=d, x="distance", y="group", col="imageid", kind="boxen", **kwargs)
            else:
                sns.catplot(data=d, x=x_axis, y=y_axis, col=facet_by, kind=plot_type, **kwargs)

        if method=='distribution':
            if x_axis is None and y_axis is None and facet_by is None and plot_type is None:
                sns.displot(data=d, x="distance", hue="imageid",  col="group", kind="kde", **kwargs)
            else:
                sns.displot(data=d, x=x_axis, hue=y_axis, col=facet_by, kind=plot_type,**kwargs)

    # return
    if return_data is True:
        return d
