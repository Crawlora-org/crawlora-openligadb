require_relative "lib/crawlora/openligadb/version"

Gem::Specification.new do |spec|
  spec.name = "crawlora-openligadb"
  spec.version = Crawlora::Openligadb::VERSION
  spec.summary = "OpenLigaDB API client for Crawlora (22 endpoints)"
  spec.description = "Ruby client for Crawlora's hosted OpenLigaDB API. Covers sports and league discovery, fixtures, match results, standings, scorers, and team match history across 22 endpoints."
  spec.authors = ["Crawlora"]
  spec.license = "MIT"
  spec.required_ruby_version = ">= 2.6"
  spec.files = Dir["lib/**/*.rb", "README.md", "CHANGELOG.md", "LICENSE"]
  spec.require_paths = ["lib"]
  spec.homepage = "https://crawlora.net/?utm_source=rubygems&utm_medium=referral&utm_campaign=platform-clients&utm_content=openligadb-ruby-homepage"
  spec.metadata = { "source_code_uri" => "https://github.com/Crawlora-org/crawlora-openligadb", "documentation_uri" => "https://github.com/Crawlora-org/crawlora-openligadb/blob/main/ruby/README.md", "rubygems_mfa_required" => "true" }

end
