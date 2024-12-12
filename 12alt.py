from utils import read_data


# Shared logic

def get_neighbours_with_same_plant(plot_plants, plot_regions, i, j):
    result = []
    for i_shift, j_shift in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        neighbour_i, neighbour_j = i + i_shift, j + j_shift
        if 0 <= neighbour_i < len(plot_plants) and \
           0 <= neighbour_j < len(plot_plants[0]) and \
           plot_plants[neighbour_i][neighbour_j] == plot_plants[i][j] and \
           plot_regions[neighbour_i][neighbour_j] is None:
                result.append((neighbour_i, neighbour_j))
    return result

def get_plot_regions_and_regions(plot_plants):
    plot_regions = [[None for _ in range(len(plot_plants[0]))] for _ in range(len(plot_plants))]
    region = 0
    regions = []

    for i in range(len(plot_plants)):
        for j in range(len(plot_plants[0])):
            if plot_regions[i][j] is not None:
                continue
            plot_regions[i][j] = region
            regions.append(region)
            last_checked_coordinates = [(i,j)]
            while len(last_checked_coordinates) > 0:
                for last_checked_i, last_checked_j in last_checked_coordinates:
                    neighbours_with_same_plant= get_neighbours_with_same_plant(plot_plants, plot_regions, last_checked_i, last_checked_j)
                    for (neighbour_i, neighbour_j) in neighbours_with_same_plant:
                        plot_regions[neighbour_i][neighbour_j] = region
                    last_checked_coordinates += neighbours_with_same_plant
                    last_checked_coordinates.remove((last_checked_i, last_checked_j))
            region += 1
    
    # Magic trick: adding padding of None region around plot 
    # to treat external perimeter as internal and skip calculating edges
    none_line = [[None] * (len(plot_regions[0]) + 2)]
    padded_plot_regions = none_line + [[None] + row + [None] for row in plot_regions] + none_line
    regions.append(None)
    return padded_plot_regions, regions


# Part 1 

plot_plants = read_data(12)
plot_regions, regions = get_plot_regions_and_regions(plot_plants)


perimeters_by_region = {region: 0 for region in regions}

for i in range(len(plot_regions)):
    for j in range(len(plot_regions[0])):
        if 1 <= i and plot_regions[i][j] != plot_regions[i - 1][j]:
            perimeters_by_region[plot_regions[i][j]] += 1
            perimeters_by_region[plot_regions[i - 1][j]] += 1
        if 1 <= j and plot_regions[i][j] != plot_regions[i][j - 1]:
            perimeters_by_region[plot_regions[i][j]] += 1
            perimeters_by_region[plot_regions[i][j - 1]] += 1


areas_by_region = {
    region: sum(row_regions.count(region) for row_regions in plot_regions) 
    for region in regions 
}


total_plot_price = sum([areas_by_region[region] * (perimeters_by_region[region]) 
                        for region in regions if region is not None])
print(total_plot_price)


# Part 2

plot_plants = read_data(12)
plot_regions, regions = get_plot_regions_and_regions(plot_plants)


horizontal_sides_by_region = {region: 0 for region in regions}

for i in range(len(plot_regions) - 1):
    previous_top_region, previous_bottom_region = None, None
    for j in range(len(plot_regions[0])):
        top_region, bottom_region = plot_regions[i][j], plot_regions[i + 1][j]
        if top_region != bottom_region:
            divide_just_started = previous_top_region == previous_bottom_region
            if previous_top_region != top_region or divide_just_started:
                horizontal_sides_by_region[top_region] += 1
            if previous_bottom_region != bottom_region or divide_just_started:
                horizontal_sides_by_region[bottom_region] += 1
        previous_top_region, previous_bottom_region = top_region, bottom_region


vertical_sides_by_region = {region: 0 for region in regions}

for j in range(len(plot_regions[0]) - 1):
    previous_left_region, previous_right_region = None, None
    for i in range(len(plot_regions)):
        left_region, right_region = plot_regions[i][j], plot_regions[i][j + 1]
        if left_region != right_region:
            divide_just_started = previous_left_region == previous_right_region
            if previous_left_region != left_region or divide_just_started:
                vertical_sides_by_region[left_region] += 1
            if previous_right_region != right_region or divide_just_started:
                vertical_sides_by_region[right_region] += 1
        previous_left_region, previous_right_region = left_region, right_region


areas_by_region = {
    region: sum(row_regions.count(region) for row_regions in plot_regions) 
    for region in regions 
}

total_plot_price = sum([areas_by_region[region] * 
                        (horizontal_sides_by_region[region] + vertical_sides_by_region[region]) 
                        for region in regions if region is not None])
print(total_plot_price)
