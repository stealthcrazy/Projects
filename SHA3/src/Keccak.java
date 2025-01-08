
public class Keccak {
	
	static State Keccak_f(State A,int NR){
		//A.displayState();
		for (int i = 0 ; i<NR;i++) {
			
			A = Rnd(A,i);
			/*A.displayState();
			System.out.println();
			System.out.println();
			System.out.println();*/
			
			
			
		}
		
		return A;
		
		
		
	}
	
	
	
	static State Rnd(State A, int Ir){
		
		A.StateArray = StepMappings.Theta(A);
		
		A.StateArray = StepMappings.Rho(A);
		A.StateArray = StepMappings.Pi(A);
		A.StateArray = StepMappings.Chi(A);
		A.StateArray = StepMappings.Iota(A,Ir);
		return A;
	}
	
}
