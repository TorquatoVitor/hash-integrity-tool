from hashlib import sha3_256, sha256, sha512
from pathlib import Path


def create_hash_object(algorithm):
    if algorithm == "1":
        return sha256()

    elif algorithm == "2":
        return sha512()

    elif algorithm == "3":
        return sha3_256()

    return None


def hash_text(text, algorithm):
    encoded_text = text.encode("utf-8")

    if algorithm == "1":
        hash_object = sha256(encoded_text)

    elif algorithm == "2":
        hash_object = sha512(encoded_text)

    elif algorithm == "3":
        hash_object = sha3_256(encoded_text)

    else:
        return None

    return hash_object.hexdigest()


def hash_file(file_path, algorithm):
    hash_object = create_hash_object(algorithm)

    if hash_object is None:
        return None

    try:
        with open(file_path, "rb") as file:
            while True:
                chunk = file.read(4096)

                if not chunk:
                    break

                hash_object.update(chunk)

        return hash_object.hexdigest()

    except PermissionError:
        print("\nPermission denied.")
        return None

    except OSError as error:
        print(f"\nError reading file: {error}")
        return None


def verify_file(file_path, expected_hash, algorithm):
    current_hash = hash_file(file_path, algorithm)

    return current_hash == expected_hash


def choose_algorithm():
    print("\nChoose algorithm:")
    print("1 - SHA-256")
    print("2 - SHA-512")
    print("3 - SHA3-256")

    while True:
        algorithm = input("\n> ")

        if algorithm in ("1", "2", "3"):
            return algorithm
        else:
            print("Invalid algorithm")


def main():
    while True:
        print("\n=====================")
        print("    HASH GENERATOR")
        print("=====================")

        print("\n1 - Hash text")
        print("2 - Hash file")
        print("3 - Verify file integrity")
        print("4 - Exit")

        option = input("\n> ")

        if option == "1":
            print("\nHash text: ")

            text = input("Text: ")
            algorithm = choose_algorithm()

            result = hash_text(text, algorithm)

            algorithm_name = get_algorithm_name(algorithm)

            print(f"\n{algorithm_name}:")
            print(result)

        elif option == "2":
            print("hash file: ")

            file_path = input("File path: ")

            if not Path(file_path).is_file():
                print("\nFile not found.")
                continue

            algorithm = choose_algorithm()

            result = hash_file(file_path, algorithm)

            if result is not None:
                algorithm_name = get_algorithm_name(algorithm)

                print(f"\n{algorithm_name}:")
                print(result)

        elif option == "3":
            print("\n--- Verify file integrity ---")

            file_path = input("File path: ")

            if not Path(file_path).is_file():
                print("\nFile not found.")
                continue

            expected_hash = input("Expected hash: ").strip().lower()

            algorithm = choose_algorithm()

            is_valid = verify_file(file_path, expected_hash, algorithm)

            if is_valid:
                print("\n[OK] File integrity verified.")
                print("The file matches the expected hash.")

            else:
                print("\n[WARNING] Integrity check failed.")
                print("The file does not match the expected hash.")

        elif option == "4":
            print("\nExiting...")
            break

        else:
            print("\nInvalid option.")


def get_algorithm_name(algortihm):
    if algortihm == "1":
        return "SHA-256"
    elif algortihm == "2":
        return "SHA-512"
    elif algortihm == "3":
        return "SHA3-256"

    return "Unknown"


if __name__ == "__main__":
    main()
