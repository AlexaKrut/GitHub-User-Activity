# GitHub User Activity

## Описание проекта
Task Tracker CLI - это проект, представляющий собой простой командный интерфейс (CLI), который позволяет пользователю вводить имя пользователя GitHub в качестве аргумента и получать информацию о его последних действиях с использованием GitHub API

## Установка

### Системные требования
- Python 3.x
- Кодовый редактор или IDE (например, VSCode, PyCharm)
- Git (для управления версиями проекта)

### Шаги установки
1. Клонируйте репозиторий проекта: 
   ```bash
   git@github.com:your username/GitHub-User-Activity.git  
2. Перейдите в папку проекта
   ```bash
   cd GitHub-User-Activity
3. Посмотрите справку о программе
   ```bash
   python3 task-cli.py -h
4. Запустите праграмму с необходимыми параметрами
   ```bash
   python3 task-cli.py <параметры>

## Использование

Запустите приложение из командной строки, указав имя пользователя GitHub

### Пример

```bash
github-activity kamranahmedse  
```

### Вывод
```bash
Pushed 1 commits to kamranahmedse/driver.js at 2024-10-20T09:12:25Z
Starred NangoHQ/nango at 2024-10-20T00:58:09Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T22:01:28Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:59:11Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:58:45Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:58:39Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:46Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:40Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:35Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:30Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:25Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:18Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:57:12Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:37:07Z
Pushed 1 commits to kamranahmedse/developer-roadmap at 2024-10-18T21:36:41Z
```

## API GitHub

Для получения информации о действиях пользователя используется следующая конечная точка:
```bash
https://api.github.com/users/<username>/events
```

## Примечание

В проекте используется сторонняя библиотека requests
Перед использованием програмы ее необходимо установить
```bash
pip install requests
```
