import math

attributes = {
    "thirsty", "nauseous", "hot"
}
examples = [
    {
        "thirsty": False,
        "nauseous": False,
        "hot": False,
        "drink": False
    },
    {
        "thirsty": True,
        "nauseous": False,
        "hot": True,
        "drink": True
    },
    {
        "thirsty": True,
        "nauseous": False,
        "hot": False,
        "drink": True
    },
    {
        "thirsty": False,
        "nauseous": True,
        "hot": True,
        "drink": False
    },
    {
        "thirsty": True,
        "nauseous": True,
        "hot": False,
        "drink": False
    }
]


# selects most common output value among set of examples
# returns True or False
def plurality_val(examples):
    count_true = 0
    count_false = 0
    for example in examples:
        if example["drink"]:
            count_true += 1
        else:
            count_false += 1
    return count_true > count_false


def all_examples_same_classification(examples):
    first_classification = examples[0]["drink"]
    for i in range(1, len(examples)):
        if examples[i]["drink"] != first_classification:
            return False
    return True


# Returns the attribute with the highest information gain
def binary_entropy(attribute, examples):
    true_probability = len([example for example in examples if example[attribute]]) / len(examples)
    false_probability = 1 - true_probability
    return - (true_probability * math.log2(true_probability) + false_probability * math.log2(false_probability))


def binary_entropy_k(probability_k):
    if probability_k == 0 or probability_k == 1:
        return 0
    return - (probability_k * math.log2(probability_k) + (1 - probability_k) * math.log2(1 - probability_k))

def remainder(attribute, examples):
    option_1_examples = [example for example in examples if example[attribute]]
    option_1_probability = len([example for example in option_1_examples if example["drink"]]) / len(examples)
    option_2_examples = [example for example in examples if not example[attribute]]
    option_2_probability = len([example for example in option_2_examples if example["drink"]]) / len(examples)

    remainder_1 = (len(option_1_examples) / len(examples)
                   * binary_entropy_k(option_1_probability / len(option_1_examples)))

    remainder_2 = (len(option_2_examples) / len(examples)
                   * binary_entropy_k(option_2_probability / len(option_2_examples)))

    return remainder_1 + remainder_2


def information_gain(attribute, examples):
    return binary_entropy(attribute, examples) - remainder(attribute, examples)


def best_information_gaining_attribute(attributes, examples):
    information_gains_per_attribute = {}
    for attribute in attributes:
        information_gains_per_attribute[attribute] = information_gain(attribute, examples)

    return max(information_gains_per_attribute, key=information_gains_per_attribute.get)


def decision_tree_learning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality_val(parent_examples)
    elif all_examples_same_classification(examples):
        # return the classification
        return examples[0]["drink"]
    elif len(attributes) == 0:
        return plurality_val(examples)
    else:
        best_attribute = best_information_gaining_attribute(attributes, examples)
        tree = Node(best_attribute, best_attribute + " = True")
        # go through all unique attributes in the best attribute
        option_1_examples = []
        option_2_examples = []
        for example in examples:
            if example[best_attribute]:
                option_1_examples.append(example)
            else:
                option_2_examples.append(example)

        subtree = decision_tree_learning(option_1_examples, attributes - {best_attribute}, examples)
        if isinstance(subtree, Node):
            subtree.label = subtree.attribute + " = True"
        tree.add_child(subtree)

        subtree = decision_tree_learning(option_2_examples, attributes - {best_attribute}, examples)
        if isinstance(subtree, Node):
            subtree.label = subtree.attribute + " = False"
        tree.add_child(subtree)
        return tree


# Node for a decision tree
class Node:

    def __init__(self, attribute, label):
        self.attribute = attribute
        self.label = label
        self.left = None
        self.right = None

    def add_child(self, node):
        if self.left is None:
            self.left = node
        else:
            self.right = node

    def print_illustration(self):
        print(self.label)
        if isinstance(self.left, Node):
            self.left.print_illustration()
        else:
            print(self.left)
        if isinstance(self.right, Node):
            self.right.print_illustration()
        else:
            print(self.right)
        pass


tree = decision_tree_learning(examples, attributes, examples)

tree.print_illustration()