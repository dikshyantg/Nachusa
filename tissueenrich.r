library(shiny)
library(TissueEnrich)

# Define UI
ui <- fluidPage(
  titlePanel("TissueEnrich Analysis"),
  sidebarLayout(
    sidebarPanel(
      textInput("gene_input", "Enter Gene Symbol (e.g., TP53):"),
      actionButton("submit_button", "Submit")
    ),
    mainPanel(
      h4("Enriched Tissues:"),
      verbatimTextOutput("enriched_tissues")
    )
  )
)

# Define server logic
server <- function(input, output) {
  # Function to run TissueEnrich analysis
  run_tissue_enrich <- function(gene_symbol) {
    enrich_results <- tissue_enrich(gene_symbol)
    return(enrich_results)
  }
  
  # Event listener for submit button
  observeEvent(input$submit_button, {
    gene_symbol <- input$gene_input
    if (gene_symbol != "") {
      output$enriched_tissues <- renderPrint({
        enrich_results <- run_tissue_enrich(gene_symbol)
        enrich_results
      })
    } else {
      output$enriched_tissues <- renderText("Please enter a gene symbol.")
    }
  })
}

# Run the application
shinyApp(ui = ui, server = server)
