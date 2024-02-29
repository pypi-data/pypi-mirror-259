import datetime as dt
import numpy as np

def parse_iso(s):
	formats = [
		'%Y-%m-%dT%H:%M:%SZ',
		'%Y-%m-%dT%H:%M:%S',
		'%Y-%m-%dT%H:%M',
		'%Y-%m-%dT%H%M%SZ',
		'%Y-%m-%dT%H%M%S',
		'%Y-%m-%dT%H%M',
		'%Y-%m-%d',
	]
	for f in formats:
		try: return dt.datetime.strptime(s, f)
		except: pass
	return None

def for_array(func):
	def f(x):
		if isinstance(x, np.ndarray):
			shape = x.shape
			res = [func(y) for y in x.flatten()]
		elif isinstance(x, (list, tuple)):
			res = [func(y) for y in x]
		elif x is np.ma.masked:
			res = x
		else:
			res = func(x)
		if isinstance(x, np.ma.core.MaskedArray):
			return np.ma.array(res, mask=x.mask).reshape(shape)
		if isinstance(x, np.ndarray):
			return np.array(res).reshape(shape)
		if isinstance(x, tuple):
			return tuple(res)
		else:
			return res
	return f

def missing(x):
	return \
		x is None or \
		x is np.ma.masked or \
		isinstance(x, float) and not np.isfinite(x) or \
		x == ''

@for_array
def from_iso(x):
	if missing(x): return np.nan
	time_dt = parse_iso(x)
	if time_dt is None: return np.nan
	return (time_dt - dt.datetime(1970,1,1)).total_seconds()/(24.0*60.0*60.0) + 2440587.5

@for_array
def to_iso(x):
	if missing(x): return None
	y = to_datetime(x)
	if y is None: return ''
	f = y.microsecond/1e6
	y += dt.timedelta(seconds=(-f if f < 0.5 else 1-f))
	return y.strftime('%Y-%m-%dT%H:%M:%S')

def to_date(x):
	try:
		n = len(x)
	except:
		date = to_date(np.array([x]))
		return [x[0] for x in date]
	cal = np.ma.ones(n, dtype=np.int8)
	year = np.ma.zeros(n, dtype=np.int32)
	month = np.ma.zeros(n, dtype=np.int8)
	day = np.ma.zeros(n, dtype=np.int8)
	hour = np.ma.zeros(n, dtype=np.int8)
	minute = np.ma.zeros(n, dtype=np.int8)
	second = np.ma.zeros(n, dtype=np.int8)
	frac = np.ma.zeros(n, dtype=np.float64)
	for i in range(n):
		if missing(x[i]):
			cal[i] = np.ma.masked
			year[i] = np.ma.masked
			month[i] = np.ma.masked
			day[i] = np.ma.masked
			hour[i] = np.ma.masked
			minute[i] = np.ma.masked
			second[i] = np.ma.masked
			frac[i] = np.ma.masked
			continue
		y = dt.datetime(1970,1,1) + dt.timedelta(days=(x[i] - 2440587.5))
		cal[i] = 1
		year[i] = y.year
		month[i] = y.month
		day[i] = y.day
		hour[i] = y.hour
		minute[i] = y.minute
		second[i] = y.second
		frac[i] = y.microsecond*1e-6
	return [cal, year, month, day, hour, minute, second, frac]

def from_date(x):
	if missing(x): return np.nan
	n = None
	try: n = len(x[0])
	except: pass
	if n is None:
		def get(a, i, b):
			return a[i] if len(a) > i else b
		return (dt.datetime(
			x[1],
			get(x, 2, 1),
			get(x, 3, 1),
			get(x, 4, 0),
			get(x, 5, 0),
			get(x, 6, 0),
			int(get(x, 7, 0)*1e6)
		) - dt.datetime(1970, 1, 1)).total_seconds()/(24*60*60) + 2440587.5
	y = np.full(n, np.nan, np.float64)
	for i in range(n):
		if any([missing(x[j][i]) for j in range(min(8, len(x)))]):
			continue
		y[i] = from_date([x[j][i] for j in range(min(8, len(x)))])
	return y

@for_array
def to_datetime(x):
	if missing(x): return None
	try:
		return dt.datetime(1970,1,1) + dt.timedelta(seconds=(x - 2440587.5)*24.0*60.0*60.0)
	except OverflowError:
		return None

@for_array
def from_datetime(x):
	if missing(x): return np.nan
	return (x - dt.datetime(1970,1,1)).total_seconds()/(24.0*60.0*60.0) + 2440587.5

@for_array
def year_day(x):
	if missing(x): return np.nan
	y = to_date(x)
	z = from_date([1, y[1], 1, 1, 0, 0, 0, 0])
	return x - z
