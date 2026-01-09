import { inject, injectable } from "inversify";
import { randomUUID } from "node:crypto";
import { TYPES } from "../../di/tokens";
import { MessagingService } from "../message/rabbitmq.service";
import { InferenceRequestType } from "../../interfaces/inference.schema"
import { FastifyBaseLogger } from "fastify";

@injectable()
export class InferenceService {
  constructor(
    @inject(TYPES.MessageBrokerService)
    private msgBrokerService: MessagingService,
    @inject(TYPES.Logger)
    private logger: FastifyBaseLogger
  ){}

  async run(request: InferenceRequestType){
    const requestId = randomUUID()
    const payload = { ...request, id: requestId };
    this.logger.info(`${this.constructor.name} publishing: ${JSON.stringify(payload)}`)

    await this.msgBrokerService.publish(payload)
    return { id: requestId, requested: true, timestamp: Date.now() }
  }
}