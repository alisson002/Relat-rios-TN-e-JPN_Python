import rpy2.robjects as robjects

def origem():
    robjects.r('''
        origem <- read.csv("origem041223.csv")
        colnames(origem) <- c("Origem", "Sessões")

        source <- origem %>% 
            filter(grepl("facebook|google|instagram|twitter|tribunadonorte|bing|yahoo|direct", Origem)) %>% 
            mutate(rede = ifelse(grepl("facebook", Origem), "Facebook", "Outro")) %>% 
            mutate(rede = ifelse(grepl("google", Origem), "Google", rede)) %>% 
            mutate(rede = ifelse(grepl("twitter", Origem), "Twitter", rede)) %>% 
            mutate(rede = ifelse(grepl("instagram", Origem), "Instagram", rede)) %>% 
            mutate(rede = ifelse(grepl("tribunadonorte", Origem), "Interno", rede)) %>% 
            mutate(rede = ifelse(grepl("bing", Origem), "Bing", rede)) %>% 
            mutate(rede = ifelse(grepl("yahoo", Origem), "Yahoo", rede)) %>% 
            mutate(rede = ifelse(grepl("direct", Origem), "Acesso direto", rede)) %>% 
            group_by(rede) %>%
            summarise(total = sum(Sessões))

        source$rede <- factor(source$rede, levels = rev(c("Acesso direto", "Google", "Instagram", "Facebook", "Twitter", "Bing", "Yahoo", "Interno")))

        source %>% 
            ggplot(aes(x = rede, y = total)) +
            geom_col(aes(fill = rede)) + coord_flip() +
            scale_fill_manual(values = c("#50bf40", "#720e9e", "#008373", "#1DA1F2", cor_fb, cor_ig, "#F4B400", "#FF4D02")) +
            labs(x = "Rede de origem", y = "Total de usuários", title="Origem dos usuário do portal") +
            theme_tufte() + theme(legend.position = "none") + scale_y_continuous(breaks = seq(0, max(500000), by = 100000))
            
        ggsave("C:/Users/Usuario/Desktop/Nova pasta/origem.png", plot = source)
    ''')