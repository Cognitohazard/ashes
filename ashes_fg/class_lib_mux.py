from ashes_fg.asic.asic_compile import *


class STD_GorS_IndirectSwitches(MUX):
    def __init__(self,circuit,island=None,num=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (0,self.num)
        self.type = "switch"
        self.name = "TSMC350nm_GorS_IndrctSwcs"
        self.Input = Port(circuit,self,"Input","N",2*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",1*self.dim[1])
        self.Vsel = Port(circuit,self,"Vsel","N",2*self.dim[1])
        self.Vg_global = Port(circuit,self,"Vg_global","N",2*self.dim[1])
        self.VTUN = Port(circuit,self,"VTUN","N",1*self.dim[1])
        self.VINJ = Port(circuit,self,"VINJ","N",1*self.dim[1])
        self.Vgrun_r = Port(circuit,self,"Vgrun_r","E",1*self.dim[0])
        self.Vgrun = Port(circuit,self,"Vgrun","W",1*self.dim[0])
        self.AVDD_r = Port(circuit,self,"AVDD_r","E",1*self.dim[0])
        self.run_r = Port(circuit,self,"run_r","E",1*self.dim[0])
        self.prog_r = Port(circuit,self,"prog_r","E",1*self.dim[0])
        self.run = Port(circuit,self,"run","W",1*self.dim[0])
        # Add cell to circuit
        circuit.addInstance(self,self.island)

class STD_IndirectGateDecoder(MUX):
    def __init__(self,circuit,island=None,bits=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = 2**(bits)/4
        self.bits = bits
        self.dim = (0,self.num)
        self.type = "decode"

        self.name = "TSMC350nm_VinjDecode2to4_htile"

        self.VGRUN = Port(circuit,self,"VGRUN","N",4*self.dim[1])
        self.RUN_OUT = Port(circuit,self,"RUN_OUT","S",4*self.dim[1])
        self.OUT = Port(circuit,self,"OUT","S",4*self.dim[1])
        self.ENABLE = Port(circuit,self,"ENABLE","N",1,static=True)
        self.VINJ_b = Port(circuit,self,"VINJ_b","S",2*self.dim[1])
        self.GND_b = Port(circuit,self,"GND_b","S",2*self.dim[1])
        self.VINJV = Port(circuit,self,"VINJV","N",1,static=True)
        self.GNDV = Port(circuit,self,"GNDV","N",1,static=True)
        self.IN = PortDecoderBit(circuit,self,"IN","W",bits)
        
        
        # Add cell to circuit
        circuit.addInstance(self,self.island)

class STD_GateMuxSWC(MUX):
    def __init__(self,circuit,island=None,num=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (0,self.num)
        self.type = "switch"

        self.name = "TSMC350nm_GateMuxSwcTile"

        self.VINJ = Port(circuit,self,"VINJ","N",2*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",2*self.dim[1])

        # Add cell to circuit
        circuit.addInstance(self,self.island)

class STD_IndirectGateSwitch(MUX):
    def __init__(self,circuit,island=None,num=1,col=-1):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (0,self.num)
        self.col = col
        self.type = "switch_ind"
        if col < 0:
            self.type = "switch"

        self.name = "TSMC350nm_IndirectSwitches"

        self.VPWR = Port(circuit,self,"VPWR","N",2*self.dim[1])
        self.RUN_IN = Port(circuit,self,"RUN_IN","N",2*self.dim[1])
        self.GND_T = Port(circuit,self,"GND_T","N",1*self.dim[1])
        self.VTUN_T = Port(circuit,self,"VTUN_T","N",1*self.dim[1])
        self.decode = Port(circuit,self,"decode","N",2*self.dim[1])
        self.VINJ_T = Port(circuit,self,"VINJ_T","N",1*self.dim[1])
        self.GND = Port(circuit,self,"GND","S",1*self.dim[1])
        self.CTRL_B = Port(circuit,self,"CTRL_B","S",2*self.dim[1])
        self.run_r = Port(circuit,self,"run_r","E",1*self.dim[1])
        self.prog_r = Port(circuit,self,"prog_r","E",1*self.dim[1])
        self.Vg = Port(circuit,self,"Vg","S",2*self.dim[1])
        self.VTUN = Port(circuit,self,"VTUN","S",1*self.dim[1])
        self.VINJ = Port(circuit,self,"VINJ","S",1*self.dim[1])
        self.VDD = Port(circuit,self,"VDD","S",2*self.dim[1])
        self.PROG = Port(circuit,self,"PROG","W",1*self.dim[0])
        self.RUN = Port(circuit,self,"RUN","W",1*self.dim[0])
        self.Vgsel = Port(circuit,self,"Vgsel","W",1*self.dim[0])
        self.vgsel_r = Port(circuit,self,"vgsel_r","E",1*self.dim[0])

        # Add cell to circuit
        circuit.addInstance(self,self.island)

class ERASE_IndirectGateSwitch(MUX):
    def __init__(self,circuit,island=None,num=0,col=-1):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (0,self.num)
        self.col = col
        self.type = "switch_ind"
        if col < 0:
            raise Exception("Specify column to erase gate switch")

        self.name = "none"

        # Add cell to circuit
        circuit.addInstance(self,self.island)


class STD_DrainDecoder(MUX):
    def __init__(self,circuit,island=None,bits=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.bits = bits
        self.num = 2**(bits-2)
        self.dim = (self.num,0)
        self.type = "decode"

        self.name = "TSMC350nm_VinjDecode2to4_vtile"

        self.VINJ = Port(circuit,self,"VINJ","N",2*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",2*self.dim[1])
        self.IN = PortDecoderBit(circuit,self,"IN","N",bits)
        self.ENABLE = Port(circuit,self,"ENABLE","W",1,static=True)

        # Add cell to circuit
        circuit.addInstance(self,self.island)

class STD_DrainSelect(MUX):
    def __init__(self,circuit,island=None,num=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (self.num,0)
        self.type = "switch"
        self.switchType = "drain_select"

        self.name = "TSMC350nm_drainSelect01d3"

        self.VINJ = Port(circuit,self,"VINJ","N",2*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",2*self.dim[1])

        # Add cell to circuit
        circuit.addInstance(self,self.island)


class STD_DrainSwitch(MUX):
    def __init__(self,circuit,island=None,num=0,VINJ=None,GND=None,Drainlines = None):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (1,self.num)
        self.type = "switch"
        self.switchType = "prog_switch"
 
        self.name = "TSMC350nm_FourTgate_ThickOx_FG_MEM"
        self.VINJ = Port(circuit,self,"VINJ","N",2*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",2*self.dim[1])
        self.Drainlines = Port(circuit,self,"B","E",4*num)

        # Initialize ports with given values
        portsInit = [VINJ,GND,Drainlines]
        i=0
        for p in self.ports:
            self.assignPort(p,portsInit[i])
            i+=1

        # Add cell to circuit
        circuit.addInstance(self,self.island)
    

class RunDrainSwitch(MUX):
    def __init__(self,circuit,island=None,num=0):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.island = island
        self.num = num
        self.dim = (self.num,0)
        self.decoder = True
        self.type = "switch"
        self.switchType = "drain_select"
 
        self.name = "TSMC350nm_drainSelect_progrundrains"
        
        self.prog_drainrail = Port(circuit,self,"prog_drainrail","N",1*self.dim[1])
        self.run_drainrail = Port(circuit,self,"run_drainrail","N",1*self.dim[1])
        self.VINJ = Port(circuit,self,"VINJ","N",1*self.dim[1])
        self.GND = Port(circuit,self,"GND","N",1*self.dim[1])

        # Add cell to circuit
        circuit.addInstance(self,self.island)


class frame(StandardCell):
    def __init__(self,circuit):
        self.circuit = circuit
        self.pins = []
        self.ports = []
        self.defaultPinLayer = "METAL3"
        self.dim = (1,1)

        self.name = "tile_analog_frame"

        circuit.frame = self

    def createPort(self,direction,name=None,dimension = 1,metal = None,connection=None):
        newPort = Port(self.circuit,self,name,direction,dimension)
        # Add metal parameter to port
        newPort.assignMetal(metal)

        if connection != None:
            newPort.connectPort(connection)

        return newPort
       
    def print(self):
        text = "\t"
        text += self.name + " " + "cab_frame("
        text += ".pin_layer(" + self.defaultPinLayer + ")"
        pNum = 0

        for port in self.ports:
            if port.isEmpty() == False:

                for i in range(port.numPins()):
                    pin = port.pins[i]
                    if pin.isConnected():
                        text += ", ." + port.location + "_" 

                        # Add port metal
                        if port.metal == None:
                            text += port.location.lower() + "_"
                        else:
                            text += port.metal + "_"

                        # Add port name
                        if port.name == None:
                            text += "p" + str(pNum)
                            pNum += 1
                        else:
                            text += port.name

                        # Add vector if necessary
                        if port.numPins() > 1:
                            text += "_" + str(i) + "_"

                        text += "("
                        text += pin.print()
                        text += ")"

        text += ");"
        
        return text
