import { FastifyInstance } from "fastify";
import { container } from "../di/container";
import { TYPES } from "../di/tokens";
import { InferenceService } from "../services/inference/inference.service";
import { InferenceRequestSchema, InferenceRequestType } from "../interfaces/inference.schema";

export const InferenceController = (app: FastifyInstance) => {
  const service = container.get<InferenceService>(TYPES.InferenceService);

  app.post("/", { schema: InferenceRequestSchema }, async (request, reply) => {
    request.log.info(`Inference: ${request.id}`)

    const response = await service.run(
      request.body as InferenceRequestType,
      request.id
    );
    return reply.status(201).send({ response })
  })
}