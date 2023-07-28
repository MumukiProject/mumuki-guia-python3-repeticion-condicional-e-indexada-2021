class Test(unittest.TestCase):

  def test_cuantas_veces_entreno_lo_suficiente_con_lista_vacia_es_0(self):
    self.assertEquals(cuantas_veces_entreno_lo_suficiente([]), 0, "cuantas_veces_entreno_lo_suficiente([]) debe devolver 0")

  def test_cuantas_veces_entreno_lo_suficiente_con_35_40_32_60_es_4(self):
    self.assertEquals(cuantas_veces_entreno_lo_suficiente([35, 40, 32, 60]), 4, "cuantas_veces_entreno_lo_suficiente([35, 40, 32, 60]) debe devolver 4")
    
  def test_cuantas_veces_entreno_lo_suficiente_con_15_45_90_0_es_2(self):
    self.assertEquals(cuantas_veces_entreno_lo_suficiente([15, 45, 90, 0]), 2, "cuantas_veces_entreno_lo_suficiente([15, 45, 90, 0]) debe devolver 2")
    
  def test_cuantas_veces_entreno_lo_suficiente_con_15_45_90_40_es_3(self):
    self.assertEquals(cuantas_veces_entreno_lo_suficiente([15, 45, 90, 40]), 3, "cuantas_veces_entreno_lo_suficiente([15, 45, 90, 40]) debe devolver 3")
        