import pandas as pd


# df = pd.DataFrame(columns=["unique_id","name","address", "designation"])
# df.to_csv("users.csv",index=False)

df = pd.read_csv("users.csv")

def add_user():
    user_name = str(input("Enter the name :"))
    user_address = str(input("Enter the address :"))
    user_designation = str(input("Enter the job designation :"))
    unique_id = len(df) + 1

    if user_name not in df["name"].values:
        df.loc[len(df)] = [unique_id, user_name, user_address, user_designation]
        df.to_csv("users.csv", index=False)
        print("user added successfully")
    else:
        print("The user name is already exists please enter new user name ")
    print()

def view_user():
    user_input = int(input("Enter the unique_id :"))
    user_data = df[df["unique_id"] == user_input]
    if not user_data.empty:
        print(user_data[["name","address", "designation"]].to_string(index=False))
        print()
    else:
        print("user id not found")

def list_users():
    print(df[["unique_id","name","address","designation"]].to_string(index=False))
    print("\n")

def update_user():
    user_input = int(input("Enter the unique_id to update :"))
    user_index = df[df["unique_id"] == user_input]


    if not user_index.empty:
        print(user_index.to_string(index=False))
        print("\nchoice to update \nName '1'\nAddress '2' \nDesignation '3'")
        update_choice = int(input("Enter your choice : "))


        if update_choice == 1:
            new_name = input("Enter the new name : ")
            if new_name not in df["name"].values:
                df.loc[user_index.index, "name"] = str(new_name)
                print("\nName updated successfully")
                print("Updated data:\n", df.loc[user_index.index])
            else:
                print("The user name already exists please enter a new user name.")
            print()
        elif update_choice == 2:
            new_address = input("Enter the new address: ")
            df.loc[user_index.index, "address"] = new_address
            print("\nAddress updated successfully")
            print("Updated data:\n", df.loc[user_index.index])

        elif update_choice == 3:
            new_designation = input("Enter the new designation: ")
            df.loc[user_index.index, "designation"] = new_designation
            print("\nDesignation updated successfully")
            print("Updated data:\n", df.loc[user_index.index])
        else:
            print("\nInvalid choice no changes were made")

        df.to_csv("users.csv", index=False)


def filter_users():

    filter_type = int(input("Enter filter type address '1' designation '2' : "))
    if filter_type == 1:
        filter_value = input("Enter address: ").strip().lower()
    else:
        filter_value = input("Enter designation: ").strip().lower()
    if filter_type == 1:
        filtered_df = df[df['address'].str.contains(filter_value,case=False)]
    elif filter_type == 2:
        filtered_df = df[df['designation'].str.contains(filter_value,case=False)]
    else:
        print("Invalid filter type Please choose 'address' or 'designation'.")
        return

    if not filtered_df.empty:
        print(filtered_df[["unique_id", "name", "address", "designation"]].to_string(index=False))
    else:
        print(f"No users found for {filter_value} in {filter_type}.")
    print()

def delete_user():
    user_input = int(input("Enter the unique_id to delete: "))
    user_index = df[df["unique_id"] == user_input]
    if not user_index.empty:
        confirm = input(f"you want to delete user {user_index['name'].values[0]}? yes/no: ").strip().lower()
        if confirm == "yes":
            df.drop(user_index.index, inplace=True)
            df.to_csv("users.csv", index=False)
            print("User deleted successfully")
        else:
            print("Operation canceled")
    else:
        print("User id not found")


while True:
    user_choice = int(input("Add new user '1' \nView details '2' "
                            "\nList all users '3'\nUpdate user details "
                            "'4'\nfilter by any '5' \ndelete user '6' \nExit '7'\nchoice : "))

    match user_choice:
        case 1:
            add_user()
        case 2:
            view_user()
        case 3:
            list_users()
        case 4:
            update_user()
        case 5:
            filter_users()
        case 6:
            delete_user()
        case 7:
            print("Exit")
            break
        case _:
            print("Invalid choice Please enter a number ")

