import 'dotenv/config'
import { app } from "./app";

const PORT: string = process.env.PORT
const HOST: string = process.env.HOST || '0.0.0.0'; 

app.listen({ 
  port: Number(PORT),
  host: HOST
})
.then(() => {
  app.log.info(`Server listening on ${HOST}:${PORT}`)
})
