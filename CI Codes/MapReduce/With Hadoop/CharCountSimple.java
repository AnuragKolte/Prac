package MapReduce;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class CharCountSimple {

    public static void main(String[] args) {
        if (args.length < 1) {
            System.out.println("Usage: java CharCountSimple <input-file>");
            return;
        }

        String inputFile = args[0];
        Map<Character, Integer> charCount = new HashMap<>();

        try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
            String line;
            while ((line = br.readLine()) != null) {
                line = line.toLowerCase().replaceAll("\\s+", "");
                for (char c : line.toCharArray()) {
                    if (Character.isLetter(c)) {
                        charCount.put(c, charCount.getOrDefault(c, 0) + 1);
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }

        // Print the character count
        for (Map.Entry<Character, Integer> entry : charCount.entrySet()) {
            System.out.println(entry.getKey() + " : " + entry.getValue());
        }
    }
}
