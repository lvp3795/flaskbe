from flask import Flask, jsonify, request
from flaskext.mysql import MySQL
from flask_restful import Resource, Api
from flask_cors import CORS
""" Khởi tạo  Flask"""
app = Flask(__name__)
CORS(app)
""" Khởi tạo MySQL"""
mysql = MySQL()

""" Khởi tạo Flask RESTful API"""
api = Api(app)

""" Kết nối cơ sở dữ liệu với backend"""
host = "u6354r3es4optspf.cbetxkdyhwsb.us-east-1.rds.amazonaws.com"
user = "p28owp7ptlkau8z7"
password = "m2mzum2vsdhlirkf"
port = 3306
database = "ogds5q1fwwemt0qz"

app.config["MYSQL_DATABASE_HOST"] = host
app.config["MYSQL_DATABASE_USER"] = user
app.config["MYSQL_DATABASE_PASSWORD"] = password
app.config["MYSQL_DATABASE_PORT"] = port
app.config["MYSQL_DATABASE_DB"] = database

""" Khởi tạo MySQL extension"""
mysql.init_app(app)


class WardList(Resource):
    """
        output: Lấy ra tất cả phường, tạo phường.
    """
    # Lấy tất cả Phường

    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `ward`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()
    # Tạo phường

    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _description = str(request.form['description'])
            create_ward_cmd = """INSERT INTO `ward`( `name`, `description`) VALUES (%s,%s)"""
            cursor.execute(create_ward_cmd, (
                _name, _description))
            conn.commit()
            response = jsonify(
                message='Created successfully!', id=cursor.lastrowid)
            # response.data = cursor.lastrowid
            response.status_code = 201
        except Exception as e:
            print(e)
            response = jsonify('Created failture!')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


class Ward(Resource):
    """
        input: ward_id.
        output: Lấy ra phường theo id, chỉnh sửa phường theo id, xoá phường theo id.
    """
    # Lấy phường theo id

    def get(self, ward_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `ward` WHERE `id`=%s""", (ward_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    # Chỉnh sửa phường theo id
    def put(self, ward_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _description = str(request.form['description'])
            update_ward_cmd = """UPDATE `ward` SET `name`=%s,`description`=%s WHERE `id`=%s"""
            cursor.execute(update_ward_cmd, (_name, _description, ward_id))
            conn.commit()
            response = jsonify('Updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Updated failture.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)

    # Delete phường theo id
    def delete(self, ward_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `ward` WHERE `id`=%s""", (ward_id))
            conn.commit()
            response = jsonify('deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed delete.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


class PlaceList(Resource):
    """
        output: Lấy ra tất cả địa điểm, tạo địa điểm mới.
    """
    # Lấy tất cả địa điểm

    def get(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute("""SELECT * FROM `place`""")
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    # Tạo địa điểm mới
    def post(self):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _description = str(request.form['description'])
            _address = str(request.form['address'])
            _map = str(request.form['map'])
            _wardId = int(request.form['wardId'])
            _type = int(request.form['type'])
            create_class_cmd = """INSERT INTO `place`( `name`, `description`, `address`,`map`,`wardId`,`type`) VALUES (%s,%s,%s,%s,%s,%s)"""
            cursor.execute(create_class_cmd, (
                _name, _description, _address, _map, _wardId, _type))
            conn.commit()
            response = jsonify(
                message='place added successfully.', id=cursor.lastrowid)
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to add place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


class Place(Resource):
    """
        input: Place_id.
        output: Lấy ra địa điểm theo id, Cập nhật địa điểm theo id, Xoá địa điểm theo id.
    """
    # lấy địa điểm theo id

    def get(self, place_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """SELECT * FROM `place` WHERE `id`=%s""", (place_id))
            rows = cursor.fetchall()
            return jsonify(rows)
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            conn.close()

    # Cập nhật địa điểm theo id
    def put(self, place_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            _name = str(request.form['name'])
            _description = str(request.form['description'])
            _address = str(request.form['address'])
            _map = str(request.form['map'])
            _wardId = int(request.form['wardId'])
            _type = int(request.form['type'])
            update_user_cmd = """UPDATE `place` SET `name`=%s,`description`=%s,`address`=%s,`map`=%s,`wardId`=%s,`type`=%s WHERE `id`=%s"""
            cursor.execute(update_user_cmd, (_name, _description,
                           _address, _map, _wardId, _type, place_id))
            conn.commit()
            response = jsonify('place updated successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to update place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)

    # Xóa địa điểm theo id
    def delete(self, place_id):
        try:
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM `place` WHERE `id`=%s""", (place_id))
            conn.commit()
            response = jsonify('place deleted successfully.')
            response.status_code = 200
        except Exception as e:
            print(e)
            response = jsonify('Failed to delete place.')
            response.status_code = 400
        finally:
            cursor.close()
            conn.close()
            return (response)


""" Danh sách routers"""
api.add_resource(WardList, '/wards', endpoint='wards')
api.add_resource(Ward, '/ward/<int:ward_id>', endpoint='ward')
api.add_resource(PlaceList, '/places', endpoint='places')
api.add_resource(Place, '/place/<int:place_id>', endpoint='place')

"""Chạy applications"""
if __name__ == "__main__":
    app.run(debug=True)
