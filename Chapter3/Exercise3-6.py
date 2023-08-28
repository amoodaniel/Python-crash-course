#Exercise3-6
print("We have a bigger space y'all!!!. More people willbe joining us.")
guest_list =['tayo', 'loren', 'pedro']
guest_list.insert(2, "Toyin")
guest_list.insert(1, "Unich")
guest_list.append("Ruger")
print(f"""you are invited {guest_list[0].title()}.\nyou are invited {guest_list[1].title()}.\
      \nyou are invited {guest_list[2].title()}\nyou are invited {guest_list[3].title()}\
      \nyou are invited {guest_list[4].title()}\nyou are invited {guest_list[-1].title()}""")