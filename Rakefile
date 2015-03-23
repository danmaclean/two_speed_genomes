
namespace :prepare_raw
  directory "cleaned"

  desc "gets all the raw pickled Python binary data for host jump and converts them to a single JSON file" 
  file "cleaned/host_jump.json" => "cleaned" do
    sh "find . -name HOST*.p | python src/pickle_to_json.py > cleaned/host_jump.json" 
  end

  desc "gets all the raw pickled Python binary data for genome lengths and converts them to a single JSON file" 
  file "cleaned/genome_lengths.json" => "cleaned" do
	  sh "find . -name LenJMP*.p | python src/pickle_to_json.py > cleaned/genome_lengths.json" 
  end

  desc "gets all the raw pickled Python binary data for population evolution and converts them to a single JSON file" 
  file "cleaned/population_evolution.json" => "cleaned" do
	  sh "find . -name PopsJMP*.p | python src/pickle_to_json.py > cleaned/population_evolution.json" 
  end

  desc "gets all the raw pickled Python binary data for reproductive rates and converts them to a single JSON file" 
  file "cleaned/reproductive_rates.json" => "cleaned" do
	  sh "find . -name RatesJMP*.p | python src/pickle_to_json.py > cleaned/reproductive_rates.json" 
  end

  desc "gets all the raw pickled Python binary data for genomes and converts them to a single JSON file" 
  file "cleaned/genomes.json" => "cleaned" do
	  sh "find . -name GenesJMP*.p | python src/pickle_to_json.py > cleaned/genomes.json" 
  end

end