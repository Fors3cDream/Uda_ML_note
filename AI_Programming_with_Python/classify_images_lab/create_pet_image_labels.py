"""
Create by Killer at 2019-04-25 17:01
"""

from os import listdir

def main():
    filename_list = listdir("pet_images/")

    print("\nPrints 10 filenames from folder pet_images/")
    for idx in range(0, 10, 1):
        print("%2d file: %-25s" % (idx+1, filename_list[idx]))

    pet_dic = dict()

    items_in_dic = len(pet_dic)
    print("\nEmpty Dictionary pet_dic - n items=", items_in_dic)

    keys = ["beagle_0239.jpg", "Boston_terrier_02259.jpg"]
    values = ["beagle", "boston terrier"]
    for idx in range(0, len(keys), 1):
        if keys[idx] not in pet_dic:
            pet_dic[keys[idx]] = values[idx]
        else:
            print("** Warning: Key=", keys[idx], "already exists in pet_dic with value = ", pet_dic[keys[idx]])

    print("\nPrinting all key-value pairs in dictionary pet_dic:")
    for key in pet_dic:
        print("Key=", key, "    Value=", pet_dic[key])

    pet_image = "Boston_terrier_02559.jpg"

    low_pet_image = pet_image.lower()

    word_list_pet_image = low_pet_image.split("_")

    pet_name = ""

    for word in word_list_pet_image:
        if word.isalpha():
            pet_name += word + " "

    pet_name = pet_name.strip()

    print("\nFilename=", pet_image,"    Label=", pet_name)


if __name__ == "__main__":
    main()