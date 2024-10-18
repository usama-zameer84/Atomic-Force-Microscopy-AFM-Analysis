def estimate_slope(curve, s, nan=float("nan")):
    distances, forces = curve
    if s == 0:
        distances, forces = distances[::-1], forces[::-1]

    # Calculating gradients
    grad = np.diff(forces) / np.diff(distances)
    steep_indx = np.where(grad < 0)[0]

    if len(steep_indx) < 2:
        return (nan, ((nan, nan), (nan, nan)), {})

    # Skiping the first part of the slops to avoid slope estimation from the initial part of slope
    # Making sure that the slope is estimated from the lower bottom part
    skip_initial = int(0.20 * len(steep_indx))
    steep_indx = steep_indx[skip_initial:]

    # Ensuring enough points are there to estimate the slope after skipping the initial part
    if len(steep_indx) < 2:
        return (nan, ((nan, nan), (nan, nan)), {})

    # Finding the longest steep segment from the lower part of the graphs
    max_length = 0
    opt_start = best_end = None
    current_strt = steep_indx[0]
    # Slope estimation 
    for i in range(1, len(steep_indx)):
        if steep_indx[i] != steep_indx[i - 1] + 1:
            current_len = steep_indx[i - 1] - current_strt
            if current_len > max_length:
                max_length = current_len
                opt_start, best_end = current_strt, steep_indx[i - 1]
            current_strt = steep_indx[i]

    if steep_indx[-1] - current_strt > max_length:
        opt_start, best_end = current_strt, steep_indx[-1]

    if opt_start is not None and best_end is not None:
        selected_distances = distances[opt_start:best_end + 1]
        selected_forces = forces[opt_start:best_end + 1]
        slope, intercept = np.polyfit(selected_distances, selected_forces, 1)
        anchors = ((selected_distances[0], selected_forces[0]), (selected_distances[-1], selected_forces[-1]))
        info = {
            'start_index': opt_start,
            'end_index': best_end,
            'slope_value': slope
        }
        return (slope, anchors, info)

    return (nan, ((nan, nan), (nan, nan)), {})
