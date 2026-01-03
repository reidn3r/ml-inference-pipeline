import { Container } from "inversify";
import { TYPES } from "./tokens";
import { InferenceService } from "../services/inference/inference.service";
import { MessagingService } from "../services/message/rabbitmq.service";

const container = new Container();
container
  .bind<InferenceService>(TYPES.InferenceService)
  .to(InferenceService)
  .inSingletonScope()

  container
  .bind<MessagingService>(TYPES.MessageBrokerService)
  .to(MessagingService)
  .inSingletonScope()

export { container };