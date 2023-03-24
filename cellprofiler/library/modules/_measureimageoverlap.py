from cellprofiler.library.functions.measurement import measure_image_overlap


def measureimageoverlap(
    ground_truth_image,
    test_image,
    mask=None,
    max_distance=250,
    penalize_missing=False,
    decimation_method="k_means",
    max_points=250,
):
    return measure_image_overlap(
        ground_truth_image,
        test_image,
        mask=mask,
        max_distance=max_distance,
        penalize_missing=penalize_missing,
        decimation_method=decimation_method,
        max_points=max_points,
    )
