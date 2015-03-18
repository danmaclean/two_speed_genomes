raw_genome_length_files = Rake::FileList["**/LenJMP*.p"]
directory "cleaned"

desc "gets all the raw pickled Python binary data and converts them to a 
single JSON file" 
file "cleaned/genome_lengths.json" => "cleaned" do
	sh "find . -name LenJMP*.p | python src/pickle_to_json.py > 	cleaned/genoms_lengths.json" 
end
