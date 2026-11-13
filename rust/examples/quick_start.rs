use crawlora_openligadb::{Client, ModelOpenligadbListResponseDoc, OpenligadbLeaguesParams};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let api_key = std::env::var("CRAWLORA_API_KEY")?;
    let client = Client::new(api_key)?;
    let response = client
        .openligadb
        .leagues(OpenligadbLeaguesParams {
            season: Some(2026),
            ..Default::default()
        })
        .await?;
    let data: ModelOpenligadbListResponseDoc = response.into_json()?;
    println!("{data:#?}");
    Ok(())
}
