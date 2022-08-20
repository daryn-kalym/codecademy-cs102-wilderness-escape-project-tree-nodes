from dialogue import *
class TreeNode:
  def __init__(self,story_piece):
    self.story_piece = story_piece
    self.choices = []
  def add_child(self,node):
    self.choices.append(node)
  def traverse(self):
    story_node = self
    print(story_node.story_piece)
    while len(story_node.choices)>0:
      choice = int(input("Enter 1 or 2 to continue the story: "))-1
      if choice not in [0,1]:
        print("Input incorrect")
      else:
        chosen_child = story_node.choices[choice]
        print(chosen_child.story_piece)
        story_node = chosen_child


user_choice = input("What is your name? ")
print(user_choice)
story_root = TreeNode(story_root_text)
print("Once upon a time…")
# print(story_root.story_piece)
choice_a = TreeNode(choice_a_text)
choice_b = TreeNode(choice_b_text)
choice_a_1 = TreeNode(choice_a_1_text)
choice_a_2 = TreeNode(choice_a_2_text)
choice_b_1 = TreeNode(choice_b_1_text)
choice_b_2 = TreeNode(choice_b_2_text)
story_root.add_child(choice_a)
story_root.add_child(choice_b)
choice_a.add_child(choice_a_1)
choice_a.add_child(choice_a_2)
choice_b.add_child(choice_b_1)
choice_b.add_child(choice_b_2)
story_root.traverse()
