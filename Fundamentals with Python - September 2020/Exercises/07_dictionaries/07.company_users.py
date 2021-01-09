def distribute_user_input_data():
    companies_users_dict = {}
    while True:
        command = input()
        if command == "End":
            return companies_users_dict
        tokens = command.split(" -> ")
        company_name = tokens[0]
        username = tokens[1]
        if company_name not in companies_users_dict.keys():
            companies_users_dict[company_name] = []
        if username not in companies_users_dict[company_name]:
            companies_users_dict[company_name].append(username)


def sort_and_print_data(companies_n_usernames):
    sorted_data = dict(sorted(companies_n_usernames.items(), key=lambda x: x[0]))
    for key, values_list in sorted_data.items():
        print(key)
        for user in values_list:
            print(f"-- {user}")


# distribute input data and returning it in dictionary
companies_n_users = distribute_user_input_data()

# sort and print the input data
sort_and_print_data(companies_n_users)
