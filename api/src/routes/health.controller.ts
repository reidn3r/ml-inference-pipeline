import { FastifyInstance } from "fastify";

export async function HealthCheckController(app: FastifyInstance) {
  app.get("/", (request, reply) => {
    app.log.info(`[HEALTHCHECK] timestamp: ${Date.now()}, date: ${new Date()}`)
    return { live: true, timestamp: Date.now(), date: new Date() }
  })  
}