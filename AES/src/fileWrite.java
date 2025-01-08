import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class fileWrite {
	fileWrite(String S , String fileName) throws IOException{
		File myFoo = new File(fileName);
		FileWriter fooWriter = new FileWriter(myFoo, false); // true to append
		                                                     // false to overwrite.
		fooWriter.write(S);
		fooWriter.close();
	}
}
