from model import Point2D

DELTA=1E300

def test_distance_classic():
    # given
    ptA = Point2D("A", 2, 8)
    ptB = Point2D("B", 5, 4)
    expectedDistance = 5.0
    # when 
    resultDistance = ptA.distance(ptB)
    # then
    assert resultDistance == expectedDistance

def test_distance_extreme():
    # given
    ptA = Point2D("A", 2E305, 8E305)
    ptB = Point2D("B", 5E305, 4E305)
    expectedDistance = 5.0E305
    # when 
    resultDistance = ptA.distance(ptB)
    # then
    assert abs(resultDistance - expectedDistance) < DELTA
    








    
    
    
    
    
    
