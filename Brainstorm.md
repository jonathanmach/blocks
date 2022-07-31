# Schemas

id: 1
title: Page
```json
[
    {"id":"title", "type": "string", "display_name": "Title"},
    {"id":"body", "type": "container", "display_name": "Body"}
]
```

id: 2
title: Settings
```json
[
    {"id":"main_nav", "type": "container", "display_name": "Main Navigation"}
    {"id":"is_right_to_left", "type": "boolean", "display_name": "Reversed layout?"}
    {"id":"footer_nav", "type": "container", "display_name": "Footer Navigation"}
    {"id":"footer_copyright", "type": "string", "display_name": "Footer Copyright"}
]
```

# Content

id: 2
name: Global settings
schema_id: 2
slug: /site-settings
parent_id: 1
```json
{
    "main_nav": [],
    "is_right_to_left": false,
    "footer_nav": [],
    "footer_copyright": "© 2022 TechMastery"

}
```
Ex: GET /v1/site-info

---

id: 2, name: Blogposts, slug: /blogposts, parent_id: 1, data: nulll
id: 3, name: My first blogposts, slug: /my-first-blogpost,  parent_id: 2, schema: 3, data: {...}
id: 4, name: My second blogposts, slug: /my-second-blogpost, parent_id: 2, schema: 3, data: {...}


# Retrieve multiple content entries
GET /v1/blogposts

---

id: 1
name: Home
schema_id: 1
slug: 

```json
{
    "title": "Home page",
    "body": [

    ]
}
```


