from core import load_data,metrics

def test_metrics():
    d=load_data()
    m=metrics(d)
    assert 0<=m['grr']<=1.1
    assert m['nrr']>0
    assert m['grade'] in 'ABCDF'
