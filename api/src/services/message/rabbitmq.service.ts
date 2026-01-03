import { injectable } from "inversify";
import Connection, { Publisher } from "rabbitmq-client";
import { InferenceRequestMessage } from "../../interfaces/inference.schema";

@injectable()
export class MessagingService {
  private conn: Connection;
  private publisher: Publisher;

  constructor(){
    this.publisher = this.connect()
  }

  async publish(data: InferenceRequestMessage){
    return this.publisher.send({
      exchange: process.env.MQ_EXCHANGE,
      routingKey: process.env.MQ_ROUTING_KEY
    },{
      id: data.id,
      model: data.model,
      content: data.text
    })
  }

  private connect(): Publisher {
    try {
      const client: Connection = new Connection(process.env.RABBITMQ_URL);

      client.on('error', (err) => {
        console.log(`[RABBITMQ]: Erro: ${err}.`)
      })

      client.on('connection', () => {
        console.log("[RABBITMQ]: Conectado.")
      })

      this.conn = client;

      const publisher: Publisher = client.createPublisher({
        confirm: true,
        maxAttempts: 3,
      })
      return publisher;
    
    } catch (error) {
      throw new Error("Erro ao conectar com RabbitMQ")
    }
  }
}