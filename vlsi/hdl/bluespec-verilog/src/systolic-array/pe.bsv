`include "params.bsv"

interface SystolicPE;
	// Compute the product of a and b, and accumulate it to the internal register
	method Action compute(Bit#(XLEN) a, Bit#(XLEN) b, Bit#(DXLEN) acc_in);

	// Return the current accumulated result
	method ActionValue#(Bit#(DXLEN)) getResult();
endinterface

module mkSystolicPE (SystolicPE);
	// Internal register to hold the accumulated result
	Reg#(Bit#(DXLEN)) acc <- mkReg(0);

	// Implement the compute method
	method Action compute(Bit#(XLEN) a, Bit#(XLEN) b, Bit#(DXLEN) acc_in);
		// Calculate product only if both a and b are non-zero to save power
		// Accumulate the product with the input accumulator
		acc <= (acc + acc_in) + ((a != 0 && b != 0) ? (zeroExtend(a) * zeroExtend(b)) : 0); 
	endmethod

	// Implement the getResult method
	method ActionValue#(Bit#(DXLEN)) getResult();
		return acc; // Return the current accumulated result
	endmethod
endmodule