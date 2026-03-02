import requests

def get_profile():
    username = input("Введите имя пользователя GitHub: ")

    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:
        print(f"\nИмя: {data.get('name', 'Не указано')}")
        print(f"Ссылка на профиль: {data.get('html_url', 'Не указано')}")
        print(f"Количество репозиториев: {data.get('public_repos', 0)}")
        print(f"Количество обсуждений: Информация недоступна через REST API")
        print(f"Количество подписок: {data.get('following', 0)}")
        print(f"Количество подписчиков: {data.get('followers', 0)}")
    else:
        print(f"Ошибка: пользователь не найден!")

def get_repositories():
    username = input("Введите имя пользователя GitHub: ")
    print("\n")

    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url)

    if repos_response.status_code == 200:
        data = repos_response.json()
        repos_list = []

        for i, repo in enumerate(data, 1):
            name = repo.get('name', 'Не указано')
            description = repo.get('description', 'Нет описания')
            language = repo.get('language', 'Не указан')
            repo_url = repo.get('html_url', '')
            repos_list.append({
                'name': name,
                'description': description,
                'language': language,
                'url': repo_url
            })
            print(f"{i}. {name}")
            if description:
                print(f"Описание: {description}")
            else:
                print("Описание: (нет описания)")
            print(f"Язык программирования: {language}")
            print(f"Ссылка: {repo_url}")

        while True:
            choice = input("Хотите найти репозиторий? (да/нет): ").lower()

            if choice == "да":
                found = False
                search_name = input("Введите название репозитория: ")
                for repo in data:
                    repo_name = repo.get('name', '')
                    if search_name in repo_name.lower():
                        if not found:
                            print("\nНайденные репозитории:")
                        print(repo_name)
                        description = repo.get('description')
                        if description:
                            print(f"Описание: {description}")
                        else:
                            print("Описание: (нет описания)")

                        print(f"Язык программирования: {language}")
                        print(f"Ссылка: {repo_url}")
                        found = True
                if not found:
                    print(f"Репозиторий не найден")
                else:
                    break

while True:
    print("1. Просмотр профиль пользователя GitHub")
    print("2. Получение всех репозиториев выбранного пользователя")
    print("3. Выход")

    user_choice = input("Выберите действие: ")

    if user_choice == "1":
        get_profile()
    elif user_choice == "2":
        get_repositories()
    elif user_choice == "3":
        print("Вы вышли")
        break
    else:
        print("Ошибка: введите 1, 2 или 3!")