from peewee import *
from playhouse.shortcuts import RetryOperationalError

class MyRetryDB(RetryOperationalError, MySQLDatabase):
    pass

database = MyRetryDB('userservicebak', **{'host': '172.21.12.120', 'password': 'tmp', 'user': 'tmp', 'charset':'utf8'})
#database = MySQLDatabase('userservicebak', **{'host': '172.21.12.120', 'password': 'tmp', 'user': 'tmp', 'charset':'utf8'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class Appinfo(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id')
    createtime = DateTimeField(db_column='createTime')
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo'
        indexes = (
            (('appinfo', 'createtime'), True),
            (('imei', 'app_pkg_name', 'app_name'), False),
        )
        primary_key = CompositeKey('appinfo', 'createtime')

class Appinfo201611(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201611'

class Appinfo201612(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201612'

class Appinfo201701(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201701'

class Appinfo201702(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201702'

class Appinfo201703(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201703'

class Appinfo201704(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201704'

class Appinfo201705(BaseModel):
    app_launch_count = IntegerField(null=True)
    app_name = CharField(null=True)
    app_pkg_name = CharField(null=True)
    app_version = CharField(null=True)
    appinfo = BigIntegerField(db_column='appinfo_id', primary_key=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)

    class Meta:
        db_table = 'appinfo_201705'

class Appinstall(BaseModel):
    app_name = CharField(null=True)
    app_pkg_name = CharField()
    createtime = DateTimeField(db_column='createTime')
    imei = CharField()
    installid = BigIntegerField()
    operate_time = CharField(null=True)
    operate_type = CharField()

    class Meta:
        db_table = 'appinstall'
        indexes = (
            (('installid', 'createtime'), True),
        )
        primary_key = CompositeKey('createtime', 'installid')

class Baseinfo(BaseModel):
    baseinfo = BigIntegerField(db_column='baseinfo_id', primary_key=True)
    brand = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    device_model = CharField(null=True)
    imei = CharField(null=True, unique=True)
    phone_hardware_version = CharField(null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'baseinfo'

class Chargeinfo(BaseModel):
    createtime = DateTimeField(null=True)
    endlevel = CharField(null=True)
    endtime = DateTimeField(null=True)
    id = BigIntegerField(primary_key=True)
    imei = CharField(null=True)
    startlevel = CharField(null=True)
    starttime = DateTimeField(null=True)

    class Meta:
        db_table = 'chargeinfo'

class Elecimage(BaseModel):
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    i = BigIntegerField(db_column='i_id', primary_key=True)
    imageurl = TextField(db_column='imageUrl', null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'elecimage'

class Electroniccard(BaseModel):
    card = BigIntegerField(db_column='card_id', primary_key=True)
    city = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    flash = CharField(null=True)
    iid = CharField(null=True)
    imei = CharField(null=True, unique=True)
    lcm = CharField(null=True)
    locationinfo = CharField(db_column='locationInfo', null=True)
    maincamera = CharField(db_column='mainCamera', null=True)
    phonemodel = CharField(db_column='phoneModel', null=True)
    phonenumber = CharField(db_column='phoneNumber', null=True)
    platformmodel = CharField(db_column='platformModel', null=True)
    province = CharField(null=True)
    repairstate = CharField(db_column='repairState', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    smscenternumber = CharField(db_column='smsCenterNumber', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    subcamera = CharField(db_column='subCamera', null=True)
    totalram = CharField(db_column='totalRam', null=True)
    totalrom = CharField(db_column='totalRom', null=True)
    upbynetwork = IntegerField(db_column='upByNetwork', null=True)
    uptype = IntegerField(db_column='upType', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'electroniccard'

class Feedbackprocess(BaseModel):
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    feedbackid = BigIntegerField(db_column='feedbackId')
    flag = CharField(null=True)
    manager = CharField(null=True)
    processid = BigIntegerField(db_column='processId', primary_key=True)
    processstate = IntegerField(null=True)
    suggestion = TextField(null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)

    class Meta:
        db_table = 'feedbackprocess'

class Imeinetwork(BaseModel):
    card = BigIntegerField(db_column='card_id')
    city = CharField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    iid = CharField(null=True)
    imei = CharField(null=True)
    locationinfo = CharField(db_column='locationInfo', null=True)
    phonenumber = CharField(db_column='phoneNumber', null=True)
    province = CharField(null=True)
    repairstate = CharField(db_column='repairState', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    smscenternumber = CharField(db_column='smsCenterNumber', null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    upbynetwork = IntegerField(db_column='upByNetwork', null=True)
    uptype = IntegerField(db_column='upType', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)

    class Meta:
        db_table = 'imeinetwork'
        primary_key = False

class Locationinfo(BaseModel):
    cid = IntegerField(null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)
    lac = IntegerField(null=True)
    latitude = FloatField(null=True)
    location = BigIntegerField(db_column='location_id', primary_key=True)
    longitude = FloatField(null=True)
    mcc = IntegerField(null=True)
    mnc = IntegerField(null=True)

    class Meta:
        db_table = 'locationinfo'

class Loginfo(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    exceptiontype = CharField(null=True)
    fileurl = CharField(null=True)
    imei = CharField()
    logid = BigIntegerField(primary_key=True)
    model = CharField(null=True)
    pkgname = CharField(null=True)

    class Meta:
        db_table = 'loginfo'

class Nation(BaseModel):
    city = CharField()
    code = CharField()
    district = CharField()
    parent = CharField()
    province = CharField()

    class Meta:
        db_table = 'nation'

class Repairrecord(BaseModel):
    barcode = CharField(null=True)
    cid = IntegerField(null=True)
    city = CharField(null=True)
    imei = CharField(null=True)
    lac = IntegerField(null=True)
    mcc = IntegerField(null=True)
    mnc = IntegerField(null=True)
    province = CharField(null=True)
    r = BigIntegerField(db_column='r_id', primary_key=True)
    repairdate = DateTimeField(null=True)
    type = IntegerField()
    wifilist = TextField(null=True)

    class Meta:
        db_table = 'repairrecord'

class Softwareversion(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)
    phone_software_version = CharField(null=True)
    softversion = BigIntegerField(db_column='softversion_id', primary_key=True)
    update_info = CharField(null=True)

    class Meta:
        db_table = 'softwareversion'

class SysDictionary(BaseModel):
    code = CharField()
    dictionarytype = IntegerField(db_column='dictionarytype_id')
    isdefault = IntegerField()
    seq = IntegerField()
    state = IntegerField()
    text = CharField()

    class Meta:
        db_table = 'sys_dictionary'

class SysDictionarytype(BaseModel):
    code = CharField()
    description = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    seq = IntegerField()

    class Meta:
        db_table = 'sys_dictionarytype'

class SysOrganization(BaseModel):
    address = CharField(null=True)
    code = CharField()
    createdatetime = DateTimeField()
    icon = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    seq = IntegerField()

    class Meta:
        db_table = 'sys_organization'

class SysResource(BaseModel):
    createdatetime = DateTimeField()
    description = CharField(null=True)
    icon = CharField(null=True)
    name = CharField()
    pid = IntegerField(null=True)
    resourcetype = IntegerField()
    seq = IntegerField()
    state = IntegerField()
    url = CharField(null=True)

    class Meta:
        db_table = 'sys_resource'

class SysRole(BaseModel):
    description = CharField(null=True)
    isdefault = IntegerField()
    name = CharField()
    seq = IntegerField()

    class Meta:
        db_table = 'sys_role'

class SysRoleResource(BaseModel):
    resource = IntegerField(db_column='resource_id')
    role = IntegerField(db_column='role_id')

    class Meta:
        db_table = 'sys_role_resource'
        indexes = (
            (('role', 'resource'), True),
        )
        primary_key = CompositeKey('resource', 'role')

class SysUser(BaseModel):
    age = IntegerField()
    createdatetime = DateTimeField()
    isdefault = IntegerField()
    loginname = CharField(unique=True)
    name = CharField()
    organization = IntegerField(db_column='organization_id')
    password = CharField()
    sex = IntegerField()
    state = IntegerField()
    usertype = IntegerField()

    class Meta:
        db_table = 'sys_user'

class SysUserRole(BaseModel):
    role = IntegerField(db_column='role_id')
    user = IntegerField(db_column='user_id')

    class Meta:
        db_table = 'sys_user_role'
        indexes = (
            (('user', 'role'), True),
        )
        primary_key = CompositeKey('role', 'user')

class Userfeedback(BaseModel):
    createtime = DateTimeField(db_column='createTime', null=True)
    imei = CharField(null=True)
    phonenumber = CharField(db_column='phoneNumber', null=True)
    problemdescription = TextField(db_column='problemDescription', null=True)
    problemtype = CharField(db_column='problemType', null=True)
    screenshot1 = TextField(null=True)
    screenshot2 = TextField(null=True)
    screenshot3 = TextField(null=True)
    softwareversion = CharField(db_column='softwareVersion', null=True)
    userfeedback = BigIntegerField(db_column='userFeedback_id', primary_key=True)

    class Meta:
        db_table = 'userfeedback'

class Warrantydate(BaseModel):
    createdate = DateTimeField(db_column='createDate', null=True)
    replacedate = IntegerField(db_column='replaceDate', null=True)
    warrantydate = IntegerField(db_column='warrantyDate', null=True)
    wid = PrimaryKeyField()

    class Meta:
        db_table = 'warrantydate'

class Website(BaseModel):
    address = CharField(null=True)
    buildtime = CharField(db_column='buildTime', null=True)
    city = CharField(null=True)
    createby = CharField(db_column='createBy', null=True)
    createtime = DateTimeField(db_column='createTime', null=True)
    email = CharField(null=True)
    fax = CharField(null=True)
    flag = CharField(null=True)
    manager = CharField(null=True)
    postalcode = CharField(db_column='postalCode', null=True)
    principal = CharField(null=True)
    province = CharField(null=True)
    site = CharField(null=True)
    siteattr = CharField(db_column='siteAttr', null=True)
    specialtype = CharField(db_column='specialType', null=True)
    supersite = CharField(db_column='superSite', null=True)
    telephone = CharField(null=True)
    updateby = CharField(db_column='updateBy', null=True)
    updatetime = DateTimeField(db_column='updateTime', null=True)
    username = CharField(db_column='userName', null=True)
    w = BigIntegerField(db_column='w_id', primary_key=True)

    class Meta:
        db_table = 'website'

