# people.py

from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

PEOPLE = {
    "Fairy":{
        "fname": "Tooth",
        "lnmae": "Fairy",
        "timestamp": get_timestamp()

    },
    "Ruprecht":{
        "fname": "Knecht",
        "lname": "Reprecht",
        "timestamp": get_timestamp()
    },
    "Bunny":{
        "fname": "Easter",
        "lname": "Bunny",
        "timestamp": get_timestamp()

    }
}

def read_all():
    return list(PEOPLE.values())

def creat_person(person):
  lname = person.get('lname')
  fname = person.get('fname')

  if lname and lname not in PEOPLE:
    PEOPLE[lname] = {
        "lname": lname,
        "fname": fname,
        "timestamp": get_timestamp()
    }
    return PEOPLE[lname], 201
  else:
    abort(
    406,
    f"Person with last name {lname} already exists",
    )

def update(lname, person):
  if lname in PEOPLE:
    PEOPLE[lname]['fname'] = person.get('fname', PEOPLE[lname]['fname'])
    PEOPLE[lname]['timestamp'] = get_timestamp()
    return PEOPLE[lname], 200
  else:
    abort(
      404,
      f"Person with last name {lname} not found"
      )

def delete(lname):
  if lname in PEOPLE:
    del PEOPLE[lname]
    return make_response(
      f"{lname} successfully deleted", 200
    )
  else:
    abort(
     404,
      f"Person with last name {lname} not found"
      )
