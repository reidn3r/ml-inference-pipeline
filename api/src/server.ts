import 'dotenv/config'
import { app } from "./app";

const PORT: string = process.env.PORT

app.listen({ port: Number(PORT) })
  .then(() => {
    console.log("[API]: Available")
    console.log(`[API]: ${PORT}`)
  })