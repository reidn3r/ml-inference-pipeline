import { Container } from "inversify";
import { TYPES } from "./tokens";
import { InferenceService } from "../services/inference/inference.service";
import { MessagingService } from "../services/message/rabbitmq.service";
import { FastifyBaseLogger } from "fastify";

const container = new Container();

container
  .bind<InferenceService>(TYPES.InferenceService)
  .to(InferenceService)
  .inSingletonScope()

container
  .bind<MessagingService>(TYPES.MessageBrokerService)
  .to(MessagingService)
  .inSingletonScope()

container
  .bind<FastifyBaseLogger>(TYPES.Logger)
  .toDynamicValue(() => {
    const { app } = require('../app');
    return app.log;
  });
  
export { container };