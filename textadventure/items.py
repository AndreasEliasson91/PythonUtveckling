items = [
    {
        "id": "id1",
        "name": "key",
        "description": "A key, strapped to a pearl necklace.",
        "actions": ["get", "drop", "check"],
        "container": False
    },
    {
        "id": "id2",
        "name": "knife",
        "description": "An rusty old knife.",
        "actions": ["get", "drop", "check"],
        "container": False
    },
    {
        "id": "id3",
        "name": "mirror",
        "description": "A broken mirror. It's written 'Belongs to Catherine' on it's back.",
        "actions": ["get", "drop", "check"],
        "container": False
    },
    {
        "id": "id4",
        "name": "chest",
        "description": "A old wooden chest. It's locked!",
        "actions": ["unlock", "lock", "check"],
        "container": True,
        "items": ["id5"]
    },
    {
        "id": "id5",
        "name": "sock",
        "description": "An old smelly sock.",
        "actions": ["get", "drop", "check"],
        "container": False
    }
]
