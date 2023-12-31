## Test API

#### Данное API предоставляет возможность получить все задачи, получить конкретную задачу, создать задачу, обновить конкретную задачу. Присутствует фильтрация по полю completed.
## Как запустить проект у себя на компьютере (Windows)
#### Клонируем репозиторий
```http
  git clone https://github.com/Sanchess58/test_api.git
```
#### Переходим в папку с проектом
```http
  cd test_api/
```
#### Создаем виртуальное окружение
```http
  python -m venv venv
```
#### Запускаем виртуальное окружение
```http
  source venv/Scripts/activate
```
#### Устанавливаем библиотеки из файла requirements.txt
```http
  pip install -r requirements.txt
```
#### Переходим в папку с файлом manage.py
```http
  cd test_api/
```
#### Выполняем миграции
```http
  python manage.py migrate
```
#### Запускаем проект
```http
  python manage.py runserver
```
## Примеры запросов

#### Страница с документацией 
```http
  GET /redoc/ или /swagger/
```
#### Получить все задачи
```http
  GET /api/tasks/
```

| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `id`      | `integer`| ID задачи           |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |
| `created_at`   | `datetime` | Дата и время создания задачи |

#### Получить все выполненные задачи 
```http
  GET /api/tasks/?completed=True
```

| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `id`      | `integer`| ID задачи           |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |
| `created_at`   | `datetime` | Дата и время создания задачи |

#### Получить все невыполненные задачи 
```http
  GET /api/tasks/?completed=False
```

| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `id`      | `integer`| ID задачи           |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |
| `created_at`   | `datetime` | Дата и время создания задачи |

#### Получить конкретную задачу
```http
GET /api/tasks/{id}/
```

| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `id`      | `integer`| ID задачи           |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |
| `created_at`   | `datetime` | Дата и время создания задачи |

### Создать задачу 

```http
POST /api/tasks/
```
| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |

### Удалить задачу

```http
DELETE /api/tasks/{id}/
```


### Обновить задачу

```http
PUT /api/tasks/{id}/
```
| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |


### Обновить задачу

```http
PUT /api/tasks/{id}/
```
| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |

### Обновить задачу частично

```http
PATCH /api/tasks/{id}/
```
| Параметр | Тип     | Описание              |
| :-------- | :------- | :------------------------- |
| `title`  | `string` | **Обязательно** Название задачи                |
| `description`    | `string` | **Обязательно** Описание задачи   |
| `completed`| `boolean` |  Завершена ли задача(по умолчанию "не завершена")       |
