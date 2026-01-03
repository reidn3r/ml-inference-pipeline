import { inject, injectable } from "inversify";
import { randomUUID } from "node:crypto";
import { TYPES } from "../../di/tokens";
import { MessagingService } from "../message/rabbitmq.service";
import { InferenceRequestType } from "../../interfaces/inference.schema"

@injectable()
export class InferenceService {
  constructor(
    @inject(TYPES.MessageBrokerService)
    private msgBrokerService: MessagingService
  ){}

  async run(request: InferenceRequestType){
    const requestId = randomUUID()
    await this.msgBrokerService.publish({ ...request, id: requestId })
    return { id: requestId, requested: true, timestamp: Date.now() }
  }
}