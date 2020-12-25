import fileinput

def day07():
    rules = {}
    for line in fileinput.input(files = ("20207.txt")):
        container, contents = parse_line(line)
        rules[container] = contents
    pt1 = len(all_containers("shiny gold", rules))
    print(f"Pt1: {pt1}")
    pt2 = bags_within("shiny gold", rules)
    print(f"Pt2: {pt2}")

def bags_within(container, rules):
    count = 0
    for rule in rules[container]:
        count += rule[0]*bags_within(rule[1], rules) + rule[0]
    return count

def all_containers(container, rules):
    containers = set()
    all_bags = containers
    for (key, value) in rules.items():
        if container in [item[1] for item in value]:
            containers.add(key)
    for value in containers:
        all_bags = all_bags | all_containers(value, rules)
    return all_bags

def parse_line(line):
    container = line.split(" contain ")[0].split(" bag")[0]
    contents_text = line.split(" contain ")[1].split(", ")
    contents = []
    for bag in contents_text:
        try:
            contents.append([
                int(bag[0]),
                bag[2:].split(" bag")[0]
            ])
        except ValueError:
            continue
    return container, contents

if __name__ == "__main__":
    day07()
