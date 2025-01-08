import java.io.FileReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;

public class fileReader {
	String text ="";
	fileReader(String fileName) throws IOException{
		
		//System.out.println("hi");
		this.text = Files.readString(Paths.get(fileName), StandardCharsets.UTF_8);
		this.text = this.text.substring(0,this.text.length());
		
		if (this.text.length() %16 != 0) {
			if (this.text.length() <16) {
				this.text += " ".repeat(16-(int)this.text.length());
			}else {
				this.text += " ".repeat(this.text.length() %16);
			}
			
			
		}
		
		
		
		
	}
	
	

}
