class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_data: list) -> list:
    for person_dict in people_data:
        Person(person_dict["name"], person_dict["age"])

    result_list = []
    for person_dict in people_data:
        person_instance = Person.people.get(person_dict["name"])

        spouse_name = person_dict.get("wife") or person_dict.get("husband")

        if spouse_name is not None:
            spouse_instance = Person.people.get(spouse_name)
            if spouse_instance:
                if "wife" in person_dict:
                    person_instance.wife = spouse_instance
                elif "husband" in person_dict:
                    person_instance.husband = spouse_instance

        result_list.append(person_instance)

    return result_list
