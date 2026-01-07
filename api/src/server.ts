import 'dotenv/config'
import { app } from "./app";

const PORT: string = process.env.PORT
const HOST: string = process.env.HOST || '0.0.0.0'; 

app.listen({ 
  port: Number(PORT),
  host: HOST
})
.then(() => {
  console.log("[API]: Available")
  console.log(`[API]: PORT ${PORT}`)
  console.log(`[API]: HOST ${HOST}`)
})