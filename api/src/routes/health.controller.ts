import { FastifyInstance } from "fastify";

export async function HealthCheckController(app: FastifyInstance) {
  app.get("/", (request, reply) => {
    return { live: true, timestamp: Date.now(), date: new Date() }
  })  
}