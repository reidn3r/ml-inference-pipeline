import { inject, injectable } from "inversify";
import Connection, { Publisher } from "rabbitmq-client";
import { InferenceRequestMessage } from "../../interfaces/inference.schema";
import { TYPES } from "../../di/tokens";
import { FastifyBaseLogger } from "fastify";

@injectable()
export class MessagingService {
  private conn: Connection;
  private publisher: Publisher;

  constructor(
    @inject(TYPES.Logger) private logger: FastifyBaseLogger
  ){
    this.publisher = this.connect()
  }

  async publish(data: InferenceRequestMessage){
    return this.publisher.send({
      exchange: process.env.MQ_EXCHANGE,
      routingKey: process.env.MQ_ROUTING_KEY
    },{
      id: data.id,
      content: data.text
    })
  }

  private connect(): Publisher {
    try {
      const client: Connection = new Connection(process.env.RABBITMQ_URL);

      client.on('error', (err) => {
        this.logger.error(`[${this.constructor.name}] RABBITMQ - Error: ${err}.`)
      })

      client.on('connection', () => {
        this.logger.info(`[${this.constructor.name}] RABBITMQ: Connected.`)
      })

      this.conn = client;

      const publisher: Publisher = client.createPublisher({
        confirm: true,
        maxAttempts: 3,
      })
      return publisher;
    
    } catch (error) {
      const msg: string = `[${this.constructor.name}] Erro while conecting to RabbitMQ`;
      this.logger.fatal({error}, msg);
      throw new Error(msg)
    }
  }
}