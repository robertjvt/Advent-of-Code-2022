import os


def draw_pixel(row_index, sprite, drawing):
    if row_index in sprite:
        drawing[row_index] = '#'
    else:
        drawing[row_index] = '.'
    return drawing, sprite


def main():
    with open (os.getcwd() + r"/day10.txt", "r") as file:
        data = file.read().splitlines()

    row_index = 0
    cycle = 1
    X = 1
    skip_current = True

    cycle_X = [(1, 1)]

    drawing = list("........................................")
    sprite = [0, 1, 2]
    drawing, sprite = draw_pixel(row_index, sprite, drawing)
    final = []

    while data != []:
        command = data[0]
        row_index += 1
        if cycle in range(40, 241, 40):
            row_index = 0
            final.append(drawing)
            drawing = list("........................................")
            sprite = [0, 1, 2]

        if command  == 'noop':
            cycle += 1
            drawing, sprite = draw_pixel(row_index, sprite, drawing)
            cycle_X.append((cycle, X))
            data.pop(0)
            continue
        
        elif 'addx' in command:
            if skip_current:
                skip_current = False
                cycle += 1
                drawing, sprite = draw_pixel(row_index, sprite, drawing)
                cycle_X.append((cycle, X))
                continue

            skip_current = True
            X += int(command.split()[1])
            sprite = [X-1, X, X+1]
            cycle += 1
            drawing, sprite = draw_pixel(row_index, sprite, drawing)
            cycle_X.append((cycle, X))
            data.pop(0)
            continue


    sum_X_cycle = 0
    for i in range(20, 221, 40):
        sum_X_cycle += (cycle_X[i-1][0]*cycle_X[i-1][1])
    print(sum_X_cycle)


    for i in final:
        print(" ".join(i))
    

if __name__ == "__main__":
    main()
