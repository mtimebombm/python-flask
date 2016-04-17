from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)

class IpForm(Form):
    ip = StringField('ip', validators=[DataRequired()])
 
class ip_profile_service:  
	ip = 0
	direction = 0
	trans_protocol_id = 0
	dst_port = 0
	all_frequency = 0
	all_up_byte = 0
	all_down_byte = 0
	eth_all_frequency = 0
	eth_all_up_byte = 0
	eth_all_down_byte = 0
	intra_all_frequency = 0
	intra_all_up_byte = 0
	intra_all_down_byte = 0
	inter_all_frequency = 0
	inter_all_up_byte = 0
	inter_all_down_byte = 0
	frequency_24_hour = []
	up_byte_24_hour = []
	down_byte_24_hour = []
	eth_frequency_24_hour = []
	eth_up_byte_24_hour = []
	eth_down_byte_24_hour = []
	intra_frequency_24_hour = []
	intra_up_byte_24_hour = []
	intra_down_byte_24_hour = []
	inter_frequency_24_hour = []
	inter_up_byte_24_hour = []
	inter_down_byte_24_hour = []
	frequency_7_day = []
	up_byte_7_day = []
	down_byte_7_day = []
	eth_frequency_7_day = []
	eth_up_byte_7_day = []
	eth_down_byte_7_day = []
	intra_frequency_7_day = []
	intra_up_byte_7_day = []
	intra_down_byte_7_day = []
	inter_frequency_7_day = []
	inter_up_byte_7_day = []
	inter_down_byte_7_day = []
	
	def __init__(self,ip,direction,trans_protocol_id,dst_port,all_frequency,all_up_byte,all_down_byte,eth_all_frequency,eth_all_up_byte,eth_all_down_byte,intra_all_frequency,intra_all_up_byte,intra_all_down_byte,inter_all_frequency,inter_all_up_byte,inter_all_down_byte,frequency_24_hour,up_byte_24_hour,down_byte_24_hour,eth_frequency_24_hour,eth_up_byte_24_hour,eth_down_byte_24_hour,intra_frequency_24_hour,intra_up_byte_24_hour,intra_down_byte_24_hour,inter_frequency_24_hour,inter_up_byte_24_hour,inter_down_byte_24_hour,frequency_7_day,up_byte_7_day,down_byte_7_day,eth_frequency_7_day,eth_up_byte_7_day,eth_down_byte_7_day,intra_frequency_7_day,intra_up_byte_7_day,intra_down_byte_7_day,inter_frequency_7_day,inter_up_byte_7_day,inter_down_byte_7_day):  
		self.ip	=	ip
		self.direction	=	direction
		self.trans_protocol_id	=	trans_protocol_id
		self.dst_port	=	dst_port
		self.all_frequency	=	all_frequency
		self.all_up_byte	=	all_up_byte
		self.all_down_byte	=	all_down_byte
		self.eth_all_frequency	=	eth_all_frequency
		self.eth_all_up_byte	=	eth_all_up_byte
		self.eth_all_down_byte	=	eth_all_down_byte
		self.intra_all_frequency	=	intra_all_frequency
		self.intra_all_up_byte	=	intra_all_up_byte
		self.intra_all_down_byte	=	intra_all_down_byte
		self.inter_all_frequency	=	inter_all_frequency
		self.inter_all_up_byte	=	inter_all_up_byte
		self.inter_all_down_byte	=	inter_all_down_byte
		self.frequency_24_hour	=	frequency_24_hour
		self.up_byte_24_hour	=	up_byte_24_hour
		self.down_byte_24_hour	=	down_byte_24_hour
		self.eth_frequency_24_hour	=	eth_frequency_24_hour
		self.eth_up_byte_24_hour	=	eth_up_byte_24_hour
		self.eth_down_byte_24_hour	=	eth_down_byte_24_hour
		self.intra_frequency_24_hour	=	intra_frequency_24_hour
		self.intra_up_byte_24_hour	=	intra_up_byte_24_hour
		self.intra_down_byte_24_hour	=	intra_down_byte_24_hour
		self.inter_frequency_24_hour	=	inter_frequency_24_hour
		self.inter_up_byte_24_hour	=	inter_up_byte_24_hour
		self.inter_down_byte_24_hour	=	inter_down_byte_24_hour
		self.frequency_7_day	=	frequency_7_day
		self.up_byte_7_day	=	up_byte_7_day
		self.down_byte_7_day	=	down_byte_7_day
		self.eth_frequency_7_day	=	eth_frequency_7_day
		self.eth_up_byte_7_day	=	eth_up_byte_7_day
		self.eth_down_byte_7_day	=	eth_down_byte_7_day
		self.intra_frequency_7_day	=	intra_frequency_7_day
		self.intra_up_byte_7_day	=	intra_up_byte_7_day
		self.intra_down_byte_7_day	=	intra_down_byte_7_day
		self.inter_frequency_7_day	=	inter_frequency_7_day
		self.inter_up_byte_7_day	=	inter_up_byte_7_day
		self.inter_down_byte_7_day	=	inter_down_byte_7_day