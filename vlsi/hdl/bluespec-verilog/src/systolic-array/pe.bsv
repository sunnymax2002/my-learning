`include "params.bsv"

interface SystolicPE;
	method Action compute(Bit#(XLEN) a, Bit#(XLEN) b, Bit#(2 * XLEN) acc_in);
		// Compute the product of a and b, and accumulate it to the internal register
	endmethod

	method ActionValue(Bit#(2 * XLEN)) getResult();
		// Return the current accumulated result
	endmethod
endinterface

module mkSystolicPE (SystolicPE);
	// Internal register to hold the accumulated result
	Reg#(Bit#(2 * XLEN)) acc <- mkReg(0);

	// Implement the compute method
	method Action compute(Bit#(XLEN) a, Bit#(XLEN) b, Bit#(2 * XLEN) acc_in);
		// Calculate product only if both a and b are non-zero to save power
		// Accumulate the product with the input accumulator
		acc <= (acc + acc_in) + ((a != 0 && b != 0) ? a * b : 0); 
	endmethod

	// Implement the getResult method
	method ActionValue(Bit#(2 * XLEN)) getResult();
		return acc; // Return the current accumulated result
	endmethod
endmodule