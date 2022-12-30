import numpy as np


def get_tiles(split_lines=False) -> dict:
    tiles = {}
    with open("day20_input.txt") as f:
        for line in f:
            if "Tile" in line:
                tile_id = int(line.split()[1].strip(":"))
                tile = []
            elif line.strip() == "":
                tiles[tile_id] = tile
            else:
                if split_lines:
                    tile.append(list(line.strip()))
                else:
                    tile.append(line.strip())
    tiles[tile_id] = tile
    return tiles


def get_edges(tiles: dict) -> dict:
    for tile_id, tile in tiles.items():
        top = tile[0]
        right = "".join([s[-1] for s in tile])
        left = "".join([s[0] for s in tile])
        bottom = tile[-1]
        tiles[tile_id] = {"top": top, "right": right, "bottom": bottom, "left": left}
    return tiles


def flip_side(s, tile):
    if s == "top" or s == "bottom":
        tmp = tile["top"]
        tile["top"] = tile["bottom"]
        tile["bottom"] = tmp
    elif s == "right" or s == "left":
        tmp = tile["right"]
        tile["right"] = tile["left"]
        tile["left"] = tmp


def rotate_sides(tile):
    tmp = tile["right"]
    tile["right"] = tile["bottom"]
    tile["bottom"] = tile["left"]
    tile["left"] = tile["top"]
    tile["top"] = tmp


def link_tiles():
    tiles = get_edges(get_tiles())
    links = {k: {"top": 0, "right": 0, "bottom": 0, "left": 0} for k in tiles.keys()}
    corner_id = []
    for tile_id, edges in tiles.items():
        common_edges = 0
        for side, edge in edges.items():
            for neighbor_id, neighbor_tile in tiles.items():
                neighbor_found = False
                if tile_id == neighbor_id:
                    continue
                for neighbor_side, neighbor_edge in neighbor_tile.items():
                    if edge == neighbor_edge or edge == neighbor_edge[::-1]:
                        common_edges += 1
                        links[tile_id][side] = neighbor_id
                        neighbor_found = True
                        break
                if neighbor_found:
                    break
        if common_edges < 3:
            corner_id.append(tile_id)
    return links, corner_id


def compose_image(corner_id, links):
    for c in corner_id:
        if not links[c]["top"] and not links[c]["left"]:
            top_right_corner = c
            break
    else:
        raise ValueError("No obvious top right corner")
    n = int(np.sqrt(len(links.keys())))
    transformations = {k: {"r": 0, "fr": 0, "ft": 0} for k in links.keys()}
    image_complete = False
    current_tile_id = top_right_corner
    row_start_id = top_right_corner
    image = [top_right_corner]
    next_idx = 1
    while not image_complete:
        next_tile_id = links[current_tile_id]["right"]
        if next_tile_id == 0:
            next_row_id = links[row_start_id]["bottom"]
            if next_row_id == 0:
                image_complete = True
                continue
            next_tile_id = next_row_id
            if row_start_id == links[next_tile_id]["left"] or row_start_id == links[next_tile_id]["right"]:
                rotate_sides(links[next_tile_id])
                transformations[next_tile_id]["r"] = 1
            if row_start_id == links[next_tile_id]["bottom"]:
                flip_side("top", links[next_tile_id])
                transformations[next_tile_id]["ft"] = 1
            if links[next_tile_id]["right"] == 0:
                flip_side("right", links[next_tile_id])
                transformations[next_tile_id]["fr"] = 1
            row_start_id = next_row_id
        else:
            if current_tile_id == links[next_tile_id]["top"] or current_tile_id == links[next_tile_id]["bottom"]:
                rotate_sides(links[next_tile_id])
                transformations[next_tile_id]["r"] = 1
            if current_tile_id == links[next_tile_id]["right"]:
                flip_side("left", links[next_tile_id])
                transformations[next_tile_id]["fr"] = 1
            if next_idx - n < 0:
                if links[next_tile_id]["top"] != 0:
                    flip_side("top", links[next_tile_id])
                    transformations[next_tile_id]["ft"] = 1
            else:
                if links[next_tile_id]["top"] != image[next_idx - n]:
                    flip_side("top", links[next_tile_id])
                    transformations[next_tile_id]["ft"] = 1
        image.append(next_tile_id)
        next_idx += 1
        current_tile_id = next_tile_id
    return image, transformations


def populate_image(image, transformations):
    n = int(np.sqrt(len(image)))
    tiles = get_tiles(split_lines=True)
    for tile_id in tiles.keys():
        if transformations[tile_id]["r"]:
            tiles[tile_id] = np.rot90(tiles[tile_id])
        if transformations[tile_id]["fr"]:
            tiles[tile_id] = np.fliplr(tiles[tile_id])
        if transformations[tile_id]["ft"]:
            tiles[tile_id] = np.flipud(tiles[tile_id])
        tiles[tile_id] = np.asarray(tiles[tile_id])[1:-1, 1:-1]
    image = np.array(image).reshape(n, n)
    image_arr = []
    for row in image:
        image_row = np.concatenate([tiles[tile_id] for tile_id in row], axis=1)
        if len(image_arr) == 0:
            image_arr = image_row
        else:
            image_arr = np.concatenate([image_arr, image_row])
    image_arr[image_arr == "#"] = 1
    image_arr[image_arr == "."] = 0
    image_arr = np.asarray(image_arr, dtype=int)

    return image_arr


def generate_monster():
    monster_str = "                  # #    ##    ##    ### #  #  #  #  #  #   "
    monster_arr = [1 if c == "#" else 0 for c in monster_str]
    monster = np.asarray(monster_arr, dtype=bool).reshape(3, -1)
    return monster


def day20_part1():
    tiles = get_edges(get_tiles())
    corner_id = []
    for tile_id, edges in tiles.items():
        common_edges = 0
        for edge in edges.values():
            for neighbor_id, neighbor_tile in tiles.items():
                neighbor_found = False
                if tile_id == neighbor_id:
                    continue
                for neighbor_edge in neighbor_tile.values():
                    if len(neighbor_edge) != len(edge):
                        continue
                    if edge == neighbor_edge or edge == neighbor_edge[::-1]:
                        common_edges += 1
                        neighbor_found = True
                        break
                if neighbor_found:
                    break
            if common_edges >= 3:
                break
        else:
            corner_id.append(tile_id)
    return np.prod(corner_id)


def day20_part2():
    links, corner_id = link_tiles()
    image, transformations = compose_image(corner_id, links)

    image_arr = populate_image(image, transformations)
    image_permutations = [image_arr, np.rot90(image_arr), np.rot90(image_arr, k=2), np.rot90(image_arr, k=3)]
    monster = generate_monster()
    monster_shape = monster.shape
    max_monsters = 0
    non_monster_ones = 0
    for im_rot in image_permutations:
        for im in [im_rot, np.fliplr(im_rot), np.flipud(im_rot)]:
            monster_ctr = 0
            for i in range(0, im.shape[0] - monster_shape[0]):
                for j in range(0, im.shape[1] - monster_shape[1]):
                    subarray = im[i:i+monster_shape[0], j:j+monster_shape[1]]
                    if (np.equal(subarray[monster], 1)).all():
                        monster_ctr += 1
            if monster_ctr > max_monsters:
                max_monsters = monster_ctr
                non_monster_ones = np.count_nonzero(im) - np.count_nonzero(monster) * max_monsters
    return non_monster_ones


if __name__ == "__main__":
    print("=" * 10 + " Part 1 " + "=" * 10)
    print(f"Product of corner tiles: {day20_part1()}")
    print("=" * 10 + " Part 2 " + "=" * 10)
    print(f" {day20_part2()}")
