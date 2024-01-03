1. Install requirements.txt by running following command:
```bash
pip install -r requirements.txt
```

2. Create .env looking like this:
```bash
DEBUG=True

DATABASE_NAME=dbname
DATABASE_USER=postgres
DATABASE_PASS=postgres
DATABASE_HOST=localhost
DATABASE_PORT=5432

SECRET_KEY=61RoEqVe^c?Im$2PMt4-vFuj@O5gPede1VT^KWenipBJ3

E_HOST_USER=someemail@gmail.com
E_HOST_PASSWORD=password
```

3. Run the app by following command:
```bash
rav run i
rav run premigrate
rav run migrate
rav run dev
```

### Now you can open 

4. Create super user to add products
```bash
rav run su
```
