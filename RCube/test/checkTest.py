'''
Created on Oct 20, 2020

@author: Cameron Holt
'''
import unittest
import RCube.check as check

class Test(unittest.TestCase):
#Happy path
    def test100_010_NominalValueOfFullCube(self):
        expectedResult = {'status':'full'}
        parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo', 'integrity': '763F71B164EF77E6916F1C2CBAEB3B2C3CA9A876AC6A94A97D6B0EF1C489E289'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_020_NominalValueOfSpotsCube(self):
        expectedResult = {'status':'spots'}
        parms = {'op': 'check', 'cube': 'rrrrbrrrryyyyryyyyoooogoooowwwwowwwwbbbbybbbbggggwgggg', 'integrity': '8BE0EEDF13B2B464A2C7A120E6104AC7039B758E93D6F65651616FBBEED9A1EF'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_030_NominalValueOfCrossesCube(self):
        expectedResult = {'status':'crosses'}
        parms = {'op': 'check', 'cube': 'ybybbbybybrbrrrbrbwgwgggwgwgogooogogryryyyryrowowwwowo', 'integrity': '3A2CA2368EDAB67D1EAB30A5DCA67757FC389AC2924E3EDAB522BAABF8403202'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_040_NominalValueOfRandomCube(self):
        expectedResult = {'status':'unknown'}
        parms = {'op': 'check', 'cube': 'bbbooooooooogggggggggrrrrrrrrrbbbbbbwwwwwwwwwyyyyyyyyy', 'integrity': 'F60549B12BC9C64FD37F15DD1CE16E16712AFC0181A84EA3898F070EBB29C60E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)

#Sad Path

    def test100_910_MissingCubeValue(self):
        expectedResult = {'status': 'error: No Cube'}
        parms = {'op': 'check', 'cube':''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_915_MissingCubeKey(self):
        expectedResult = {'status': 'error: No Cube'}
        parms = {'op': 'check'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_920_IncorrectNumberOfElements(self):
        expectedResult = {'status': 'error: Wrong number of faces'}
        parms = {'op': 'check', 'cube' :'11111111122222222233333333344444444455555555566666666', 'integrity': '825E9253B6D7DB91050DA156E2CF524AE9B532B0C9C3DF89B01F18592850D5D3'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_925_IncorrectNumberOfColors(self):
        expectedResult = {'status': 'error: Incorrect number of colors'}
        parms = {'op': 'check', 'cube' :'111111111222222222333333333444444444555555555111111111', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_930_TooManyCubies(self):
        expectedResult = {'status': 'error: Wrong number of faces'}
        parms = {'op': 'check', 'cube' :'1111111112222222223333333334444444445555555556666666667', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_931_TooManyColors(self):
        expectedResult = {'status': 'error: Incorrect number of colors'}
        parms = {'op': 'check', 'cube' :'178911112222222223333333334444444445555555556666666667', 'integrity': '93C6A03A7B2F9F5D319128523FA96AB3C748C67EAA6FDD4DAC8311F4D0393921'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_935_TooManyofOneColor(self):
        expectedResult = {'status': 'error: Incorrect number of colors'}
        parms = {'op': 'check', 'cube' :'111111111222222222333333333444444444555555555666666665', 'integrity': 'FFFA07BE4BF1438C0C660DE9E9C0624640DC23856E875F6730F6195CEAF2AB61'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_940_NoDistinctMiddle(self):
        expectedResult = {'status': 'error: Indistinct middle'}
        parms = {'op': 'check', 'cube' :'111141111222222222333333333144444444555555555666666666', 'integrity': 'A76983334BA3061D574662C5329E509475845E980971BC0ED0B5288FE2757C31'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)    
    
    def test100_950_ImpossibleCorner(self):
        expectedResult = {'status': 'error: Impossible corner'}
        parms = {'op': 'check', 'cube' :'bbgbbbbbbwoooooooogogggggggrrrrrrrrrwwwwwwwwbyyyyyyyyy', 'integrity': '573D39853F85AFD6E55A0760EFA1EBE8A7EACA41753055D9B41D0B3FC5C2E986'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
         
    def test100_955_ImpossibleEdge(self):
        expectedResult = {'status': 'error: Impossible edge'}
        parms = {'op': 'check', 'cube' :'gggggggggrrrrrrrrrbbbbbbbybooooooooowwwwwwwwwybyyyyyyy', 'integrity': '96DDC169F9D847DC098BA3805C1AD55B088293F0138D7D1603C03543F7D5589E'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
#     
    def test100_960_DoesNotMatchIntegrityValue(self):
        expectedResult = {'status': 'error: Wrong Integrity Value'}
        parms = {'op': 'check', 'cube' :'111111111222222222333333333444444444555555555666666666', 'integrity': '88d897bd22e132d21a538745e63995b07d7c52ce9617a0979520545753ee0ded'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_965_NoIntegrityValue(self):
        expectedResult = {'status': 'error: No Integrity Value'}
        parms = {'op': 'check', 'cube' :'111111111222222222333333333444444444555555555666666666', 'integrity': ''}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
    def test100_970_NoIntegrityValue(self):
        expectedResult = {'status': 'error: No Integrity Value'}
        parms = {'op': 'check', 'cube' :'111111111222222222333333333444444444555555555666666666'}
        actualResult = check._check(parms)
        self.assertDictEqual(expectedResult, actualResult)
        
#Corner Tests
    def test200_200_CornerCheckValidation(self):
        expectedResult = {'status': 'Corner exists'}
        #parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'}
        cube = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'
        actualResult = check._checkCorner(cube)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test200_210_CornersInvalid(self):
        expectedResult = {'status': 'error: Impossible corner'}
        #parms = {'op': 'check', 'cube': 'gggggggggwyyyyyyyybbbbbbbbbwwywwwwwwrrrrrrrrrooooooooo'}
        cube = 'gggggggggwyyyyyyyybbbbbbbbbwwywwwwwwrrrrrrrrrooooooooo'
        actualResult = check._checkCorner(cube)
        self.assertDictEqual(expectedResult, actualResult)
    
#Edge Tests
    def test100_300_EdgeCheckValidation(self):
        expectedResult = {'status': 'Edge exists'}
        #parms = {'op': 'check', 'cube': 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'}
        cube = 'gggggggggyyyyyyyyybbbbbbbbbwwwwwwwwwrrrrrrrrrooooooooo'
        actualResult = check._checkEdge(cube)
        self.assertDictEqual(expectedResult, actualResult)
    
    def test100_310_EdgeCheckInValid(self):
        expectedResult = {'status': 'error: Impossible edge'}
        #parms = {'op': 'check', 'cube': 'gggggbgggyyyyyyyyybbbbbgbbbwwwwwwwwwrrrrrrrrrooooooooo'}
        cube = 'gwwrgyobwogwwwwboybrbgbrgrwroowybrgbyyoyoyobgyyrorbggr'
        actualResult = check._checkEdge(cube)
        self.assertDictEqual(expectedResult, actualResult)
        